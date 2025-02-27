import csv
import json

from models.Output import Chapter, Group, Question


def load_data_model() -> list[Chapter]:
    with open("data.json") as data_json:
        data: str = data_json.read()
        data = data.replace("\n", "<br>")
        chapters_json = json.loads(data)
    return [Chapter(**chapter) for chapter in chapters_json]


def parse_options(options: list[str]) -> str:
    if not options:
        return ""
    option_lines: list[str] = []
    OPTION_NAMES: list[str] = ["a", "b", "c", "d", "e"]
    try:
        for optionIdx, option in enumerate(options):
            option_lines.append(f"({OPTION_NAMES[optionIdx]}) {option}")
    except IndexError as e:
        print(f"{options=}")
        raise (e)
    return "<br>".join(option_lines)


def parse_item(deck_name: str, item: Group | Question) -> list[list[str]]:
    rows: list[list[str]] = []
    if isinstance(item, Group):
        for question in item.questions:
            front: str = item.parent_question + "<br><br>"
            front += question.question + "<br><br>"
            if question.options:
                options: str = parse_options(question.options)
                front += options
            rows.append([deck_name, front, question.correct_option])
    else:
        assert(isinstance(item, Question))
        front: str = item.question + "<br><br>"
        assert item.options is not None
        options: str = parse_options(item.options)
        front += options
        rows = [[deck_name, front, item.correct_option]]
    return rows

def parse_into_2d(model: list[Chapter]) -> list[list[str]]:
    rows: list[list[str]] = []
    for chapter in model:
        for problem_type in chapter.types:
            deck_name: str = f"{chapter.chapter_name}::{problem_type.type_name}"
            for case in problem_type.cases:
                if case.case_name:
                    deck_name = f"{chapter.chapter_name}::{problem_type.type_name}::{case.case_name}"
                for item in case.items:
                    rows += parse_item(deck_name, item)
    return rows


def create_importable_file(data: list[list[str]]):
    with open("anki.csv", "w") as a_csv:
        a_csv.write("#separator:comma\n")
        a_csv.write("#html:true\n")
        a_csv.write("#deck column:1\n")
        writer = csv.writer(a_csv)
        writer.writerows(data)


def main():
    model: list[Chapter] = load_data_model()
    data: list[list[str]] = parse_into_2d(model)
    create_importable_file(data)


if __name__ == "__main__":
    main()
