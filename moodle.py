import json

import xml.etree.ElementTree as ET

from models.Output import Chapter, Group, Question


def load_chapters() -> list[Chapter]:
    with open("data.json") as data_json:
        data: str = data_json.read()
        data = data.replace("\\n", "<br>")
        chapters_json = json.loads(data)
    return [Chapter(**chapter) for chapter in chapters_json]


def create_options(question_element: ET.Element, options: list[str] | None, correct_option: str) -> None:
    if options is not None:
        for option_idx in range(len(options)):
            answer_element: ET.Element = ET.SubElement(question_element, "answer")
            answer_element.attrib["fraction"] = (
                "100" if ord(correct_option) - 97 == option_idx else "0"
            )
            ET.SubElement(answer_element, "text").text = options[option_idx]
    else:
        for option_idx in range(5):
            answer_element: ET.Element = ET.SubElement(question_element, "answer")
            answer_element.attrib["fraction"] = (
                "100" if ord(correct_option) - 97 == option_idx else "0"
            )
            ET.SubElement(answer_element, "text").text = " "


def create_question(
    root: ET.Element, question: str, options: list[str] | None, correct_option: str
) -> None:
    question_element: ET.Element = ET.SubElement(root, "question")
    question_element.attrib["type"] = "multichoice"

    name_element: ET.Element = ET.SubElement(question_element, "name")
    ET.SubElement(name_element, "text").text = question

    questiontext_element: ET.Element = ET.SubElement(question_element, "questiontext")
    questiontext_element.attrib["format"] = "html"
    ET.SubElement(questiontext_element, "text").text = question

    create_options(question_element, options, correct_option)

    ET.SubElement(question_element, "single").text = "true"
    ET.SubElement(question_element, "answernumbering").text = "abc"


def parse_item(root: ET.Element, item: Group | Question):
    if isinstance(item, Group):
        for question in item.questions:
            create_question(
                root,
                item.parent_question + "<br><br>" + question.question,
                question.options,
                question.correct_option,
            )
    else:
        assert isinstance(item, Question)
        create_question(root, item.question, item.options, item.correct_option)


def create_xml_tree(chapters: list[Chapter]) -> ET.ElementTree:
    root: ET.Element = ET.Element("quiz")
    for chapter in chapters:
        for problem_type in chapter.types:
            for case in problem_type.cases:
                for item in case.items:
                    parse_item(root, item)
    return ET.ElementTree(root)


def create_importable_file(xml_tree: ET.ElementTree):
    ET.indent(xml_tree, space="  ")
    with open("moodle.xml", "wb") as moodle_xml:
        moodle_xml.write(b'<?xml version="1.0" ?>')
        xml_tree.write(moodle_xml, encoding="utf-8")


def main():
    chapters: list[Chapter] = load_chapters()
    xml_tree: ET.ElementTree = create_xml_tree(chapters)
    create_importable_file(xml_tree)


if __name__ == "__main__":
    main()
