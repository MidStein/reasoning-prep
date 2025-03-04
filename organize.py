import importlib
import json
import os

import models.Input as Input
import models.Output as Output

REASONING_DIR: str = os.path.dirname(__file__)
CHAPTER_PATH_DICT: dict[str, str] = {
    "Series Completion": "series_completion",
    "Coding - Decoding": "coding_decoding",
    "Blood Relations": "blood_relations",
    "Puzzle Test": "puzzle_test",
    "Sequential Output Tracing": "sequential_output_tracing",
    "Direction Sense Test": "direction_sense_test",
    "Alphabet Test": "alphabet_test",
    "Number, Ranking & Time Seqeunce Test": "number_ranking_and_time_sequence_test",
    "Data Sufficiency": "data_sufficiency",
    "Logic": "logic",
}
chapter_module_dict: dict[str, tuple[list[Input.Type], list[list[str]]]] = {}


def parse_options_file(chapter_dir_name: str, exercise_name: str) -> list[list[str]]:
    with open(
        f"{REASONING_DIR}/{chapter_dir_name}/options/{exercise_name}.txt"
    ) as options_txt:
        file_contents: str = options_txt.read()
    options: list[list[str]] = [
        group.split("\n") for group in file_contents.split("\n\n")
    ]
    assert not options[-1][-1]
    del options[-1][-1]
    return options


def load_group(
    group: Input.Group, options: list[list[str]], correct_options: list[str]
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
        except IndexError as e:
            # print(group.from_question - 1 + question_idx)
            raise(e)
    return Output.Group(
        parent_question=group.parent_question,
        questions=questions,
    )


def load_case_items(
    input_chapter: str,
    case: Input.Case,
    case_letter_idx: int,
) -> list[Output.Group | Output.Question]:
    options: list[list[str]] = parse_options_file(
        CHAPTER_PATH_DICT[input_chapter], chr(case_letter_idx + 97)
    )
    correct_options: list[str] = chapter_module_dict[input_chapter][1][case_letter_idx]

    items: list[Output.Group | Output.Question] = []
    for input_item in case.items:
        try:
            if isinstance(input_item, Input.Group):
                group: Output.Group = load_group(input_item, options, correct_options)
                items.append(group)
            else:
                    question: Output.Question = Output.Question(
                        question=input_item.question,
                        options=options[input_item.number - 1],
                        correct_option=correct_options[input_item.number - 1],
                    )
                    items.append(question)
        except IndexError as e:
            print(case.case_name)
            raise(e)
    return items


def main():
    for key, value in CHAPTER_PATH_DICT.items():
        if key in ["Series Completion", "Coding - Decoding"]:
            types_module = importlib.import_module(f"{value}.types")
            correct_options_module = importlib.import_module(f"{value}.correct_options")
            chapter_module_dict[key] = (
                getattr(types_module, "TYPES"),
                getattr(correct_options_module, "CORRECT_OPTIONS"),
            )

    chapters: list[Output.Chapter] = []
    for input_chapter in CHAPTER_PATH_DICT.keys():
        if input_chapter in ["Series Completion", "Coding - Decoding"]:
            types: list[Output.Type] = []
            case_letter_idx: int = 0
            for input_problem_type in chapter_module_dict[input_chapter][0]:
                cases: list[Output.Case] = []
                for case_idx in range(len(input_problem_type.cases)):
                    input_case: Input.Case = input_problem_type.cases[case_idx]
                    try:
                        items: list[Output.Group | Output.Question] = load_case_items(
                            input_chapter, input_case, case_letter_idx
                        )
                    except IndexError as e:
                        print(chapter_module_dict[input_chapter][1][2])
                        raise(e)
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

    with open(f"{REASONING_DIR}/data.json", "w") as output_json:
        json.dump(
            [chapter.model_dump() for chapter in chapters],
            output_json,
            indent=2,
        )


if __name__ == "__main__":
    main()
