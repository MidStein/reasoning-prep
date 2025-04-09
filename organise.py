import importlib
import json
import logging
import os
import sys
from typing import TypedDict

import models.Input as Input
import models.Output as Output

BASE_DIR: str = os.path.dirname(__file__)
CHAPTER_PATH_DICT: dict[str, str] = {
    "Series Completion": "series_completion",
    "Coding - Decoding": "coding_decoding",
    "Blood Relations": "blood_relations",
    "Puzzle Test": "puzzle_test",
    "Sequential Output Tracing": "sequential_output_tracing",
    "Direction Sense Test": "direction_sense_test",
    "Alphabet Test": "alphabet_test",
    "Number, Ranking & Time Sequence Test": "number_ranking_and_time_sequence_test",
    "Data Sufficiency": "data_sufficiency",
    "Logic": "logic",
}


class TypesAndCorrectOptions(TypedDict):
    types: list[Input.Type]
    correct_options: list[list[str]]


def get_chapter_attributes() -> dict[str, TypesAndCorrectOptions]:
    chapter_attributes: dict[str, TypesAndCorrectOptions] = {}
    for key, value in CHAPTER_PATH_DICT.items():
        types_module = importlib.import_module(f"chapters.{value}.types")
        correct_options_module = importlib.import_module(f"chapters.{value}.correct_options")
        chapter_attributes[key] = {
            "types": getattr(types_module, "TYPES"),
            "correct_options": getattr(correct_options_module, "CORRECT_OPTIONS"),
        }
    return chapter_attributes


def parse_options_file(chapter_dir_name: str, exercise_name: str) -> list[list[str]]:
    with open(
        f"{BASE_DIR}/chapters/{chapter_dir_name}/options/{exercise_name}.txt"
    ) as options_txt:
        file_contents: str = options_txt.read()
    options: list[list[str]] = [
        group.split("\n") for group in file_contents.split("\n\n")
    ]
    assert not options[-1][-1]
    del options[-1][-1]
    return options


def load_group(
    group: Input.Group,
    options: list[list[str]],
    correct_options: list[str],
) -> Output.Group:
    questions: list[Output.Question] = []
    for question_idx in range(len(group.questions)):
        try:
            question: Output.Question = Output.Question(
                question=group.questions[question_idx],
                options=None
                if group.no_options
                else options[group.from_question - 1 + question_idx],
                correct_option=correct_options[group.from_question - 1 + question_idx],
            )
            questions.append(question)
        except IndexError:
            logging.debug(f"{group.from_question=}")
            logging.debug(f"{group.from_question + question_idx=}")
            logging.debug(f"{len(options)=}")
            logging.debug(f"{len(correct_options)=}")
            raise
    return Output.Group(
        parent_question=group.parent_question,
        questions=questions,
    )


def load_case_items(
    input_chapter: str,
    case: Input.Case,
    case_letter_idx: int,
    chapter_attributes: dict[str, TypesAndCorrectOptions],
) -> list[Output.Group | Output.Question]:
    options: list[list[str]] = parse_options_file(
        CHAPTER_PATH_DICT[input_chapter], chr(case_letter_idx + 97)
    )
    correct_options: list[str] = chapter_attributes[input_chapter]["correct_options"][
        case_letter_idx
    ]
    num_of_questions: int = 0
    items: list[Output.Group | Output.Question] = []
    for input_item in case.items:
        try:
            if isinstance(input_item, Input.Group):
                if not input_item.skip:
                    group: Output.Group = load_group(input_item, options, correct_options)
                    items.append(group)
                num_of_questions += len(input_item.questions)
            else:
                if input_item.skip:
                    num_of_questions += 1
                    continue
                question: Output.Question = Output.Question(
                    question=input_item.question,
                    options=options[input_item.number - 1],
                    correct_option=correct_options[input_item.number - 1],
                )
                items.append(question)
                num_of_questions += 1
        except IndexError:
            logging.debug(f"{case.case_name=}")
            raise

    if num_of_questions != len(correct_options):
        logging.debug(f"{num_of_questions=}")
        logging.debug(f"{len(correct_options)=}")
        logging.debug(f"{len(options)=}")
        if isinstance(items[-1], Output.Question):
            logging.debug(f"{items[-1].question=}")
        else:
            logging.debug(f"{items[-1].parent_question=}")
        raise Exception
    return items


def main():
    if os.path.exists(os.path.expanduser("~/tbd/debug.log")):
        logging.basicConfig(
            filename=os.path.expanduser("~/tbd/debug.log"),
            filemode="w",
            level=logging.DEBUG,
            format="%(lineno)d: %(message)s",
        )
    else:
        logging.basicConfig(
            filename="debug.log",
            filemode="w",
            level=logging.DEBUG,
            format="%(lineno)d: %(message)s",
        )


    chapter_module_dict: dict[str, TypesAndCorrectOptions] = get_chapter_attributes()

    chapters: list[Output.Chapter] = []
    for input_chapter in CHAPTER_PATH_DICT.keys():
        types: list[Output.Type] = []
        case_letter_idx: int = 0
        for input_problem_type in chapter_module_dict[input_chapter]["types"]:
            cases: list[Output.Case] = []
            for case_idx in range(len(input_problem_type.cases)):
                input_case: Input.Case = input_problem_type.cases[case_idx]
                try:
                    items: list[Output.Group | Output.Question] = load_case_items(
                        input_chapter, input_case, case_letter_idx, chapter_module_dict
                    )
                except IndexError or AssertionError:
                    logging.debug(f"{input_chapter=}")
                    logging.debug(f"{input_problem_type.type_name=}")
                    logging.debug(f"{case_letter_idx=}")
                    raise
                case: Output.Case = Output.Case(
                    case_name=input_case.case_name, items=items
                )
                cases.append(case)
                case_letter_idx += 1
            problem_type: Output.Type = Output.Type(
                type_name=input_problem_type.type_name, cases=cases
            )
            types.append(problem_type)
        chapter: Output.Chapter = Output.Chapter(
            chapter_name=input_chapter, types=types
        )
        chapters.append(chapter)

    with open(f"{BASE_DIR}/data.json", "w") as output_json:
        json.dump(
            [chapter.model_dump() for chapter in chapters],
            output_json,
            indent=2,
        )


if __name__ == "__main__":
    main()
