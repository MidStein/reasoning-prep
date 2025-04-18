import csv
import json

from models.Output import Chapter, Group, Question


def load_data_model() -> list[Chapter]:
    with open("data.json") as data_json:
        data: str = data_json.read()
        chapters_json = json.loads(data)
    return [Chapter(**chapter) for chapter in chapters_json]


def parse_options(options: list[str]) -> str:
    if not options:
        return ""
    option_lines: list[str] = []
    OPTION_NAMES: list[str] = ["a", "b", "c", "d", "e"]
    try:
        for option_idx, option in enumerate(options):
            option_lines.append(
                "<input type='radio' name='selected_option' />"
                + f"({OPTION_NAMES[option_idx]}) {option}"
            )
    except IndexError as e:
        print(f"{options=}")
        raise (e)
    return "<br>".join(option_lines)


def parse_item(deck_name: str, item: Group | Question) -> list[list[str]]:
    rows: list[list[str]] = []
    if isinstance(item, Group):
        for question in item.questions:
            if question.options:
                options: str = parse_options(question.options)
                rows.append(
                    [
                        "group",
                        deck_name,
                        item.parent_question,
                        question.question,
                        options,
                        question.correct_option,
                    ]
                )
            else:
                rows.append(
                    [
                        "group2",
                        deck_name,
                        item.parent_question,
                        question.question,
                        question.correct_option,
                    ]
                )
    else:
        assert isinstance(item, Question)
        assert item.options is not None
        options: str = parse_options(item.options)
        rows = [
            [
                "individual_question",
                deck_name,
                item.question,
                options,
                item.correct_option,
            ]
        ]
    return rows


def parse_into_2d(model: list[Chapter]) -> list[list[str]]:
    rows: list[list[str]] = []
    for chapter in model:
        for problem_type in chapter.types:
            deck_name: str = (
                f"Reasoning::{chapter.chapter_name}::{problem_type.type_name}"
            )
            for case in problem_type.cases:
                if case.case_name:
                    deck_name = f"Reasoning::{chapter.chapter_name}::{problem_type.type_name}::{case.case_name}"
                for item in case.items:
                    rows += parse_item(deck_name, item)
    return rows


def create_importable_file(data: list[list[str]]):
    with open("anki.csv", "w") as a_csv:
        a_csv.write("#separator:comma\n")
        a_csv.write("#html:true\n")
        a_csv.write("#notetype column:1\n")
        a_csv.write("#deck column:2\n")
        writer = csv.writer(a_csv)
        writer.writerows(data)


def main():
    model: list[Chapter] = load_data_model()
    data: list[list[str]] = parse_into_2d(model)
    create_importable_file(data)


if __name__ == "__main__":
    main()
