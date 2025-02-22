# import json

from typing import Any

# from model.Reasoning import Group, Question


QUESTIONS: Any = [
    {
        "parent_question": "Directions : In each of the following questions, a number series is given with one term missing. Choose the correct alternative that will continue the same pattern and fill in the blank spaces.",
        "questions": [
            "1, 4, 9, 16, 25, (.....)",
            "20, 19, 17, (.....), 10, 5",
            "2, 3, 5, 7, 11, (.....), 17",
            "6, 11, 21, 36, 56, (.....)",
            "1, 6, 13, 22, 33, (.....)",
            "3, 9, 27, 81, (.....)",
            "1, 9, 17, 33, 49, 73, (.....)",
            "2, 5, 9, (.....), 20, 27",
            "5, 9, 17, 29, 45, (.....)",
            "3, 7, 15, 31, 63, (.....)",
            "1, 6, 15, (.....), 45, 66, 91",
            "1, 2, 3, 5, 8, (.....)",
            "0.5, 1.5, 4.5, 13.5, (.....)",
            "121, 225, 361, (.....)",
            "0, 2, 8, 14, (.....), 34",
            "19, 2, 38, 3, 114, 4, (.....)",
            "1, 2, 3, 6, 9, 18, (.....), 54",
            "4, 5, 9, 18, 34, (.....)",
            "3, 6, 18, 72, (.....)",
            "66, 36, 18, (.....)",
            "21, 25, 33, 49, 81, (.....)",
            "12, 32, 72, 152, (.....)",
            "3, 6, 5, 20, 7, 42, 9, (.....)",
            "1, 3, 4, 8, 15, 27, (.....)",
            "2, 15, 41, 80, (.....)",
            "8, 10, 14, 18, (.....), 34, 50, 66",
            "1, 2, 6, 24, (.....)",
            "2, 3, 8, 63, (.....)",
            "95, 115.5, 138, (.....), 189",
            "4, 10, (.....), 82, 244, 730",
            "4, 32, 128, (.....)",
            "2, 5, 9, 19, 37, (.....)",
            "24, 60, 120, 210, (.....)",
            "165, 195, 255, 285, 345, (.....)",
            "5, 17, 37, 65, (.....), 145",
            "9, 11, 20, 31, (.....), 82",
            "5, 16, 49, 104, (.....)",
            "34, 18, 10, 6, 4, (.....)",
            "462, 420, 380, (.....), 306",
            "3, 8, 22, 63, 185, (.....)",
            "1, 2, 5, 12, 27, 58, 121, (.....)",
            "0.5, 0.55, .65, 0.8, (.....)",
            "3, 8, 13, 24, 41, (.....)",
            "97, 86, 73, 58, 45, (.....)",
            "17, 19, 23, 29, (.....), 37",
            "5, 6, 9, 15, (.....), 40",
            "3, 12, 27, 48, 75, 108, (.....)",
            "134, 245, 356, 467, (.....)",
            "6, 13, 28, (.....)",
            "563, 647, 479, 815, (.....)",
            "11, 12, 17, 18, 23, 24, (.....)",
            "225, 336, 447, (.....), 669, 7710",
            "840, 168, 42, 14, 7, (.....)",
            "5, 6, 7, 8, 10, 11, 14, (.....)",
            "0, 2, 3, 5, 8, 10, 15, 17, 24, 26, (.....)",
            "0, 4, 6, 3, 7, 9, 6, (.....), 12",
            "1, 1, 3, 9, 6, 36, 10, 100, (.....), 225",
            "2, 1, 2, 4, 4, 5, 6, 7, 8, 8, 10, 11, (.....)",
            "4, 23, 60, 121, (.....)",
            "1, 4, 2, 8, 6, 24, 22, 88, (.....)",
            "13, 32, 24, 43, 35, (.....), 46, 65, 57, 76",
            "3, 4, 7, 7, 13, 13, 21, 22, 31, 44, (.....)",
            "2, 6, 12, 20, 30, 42, 56, (.....)",
            "8, 9, 8, 7, 10, 9, 6, 11, 10, (.....), 12",
            "90, 180, 12, 50, 100, 200, (.....), 3, 50, 4, 25, 2, 6, 30, 3",
            "11, 10, (.....), 100, 1001, 1000, 10001",
            "123456147, 12345614, 2345614, 234561, (.....)",
            "\\(\\frac{4}{9}\\), \\(\\frac{9}{20}\\), \\(\\frac{39}{86}\\)",
            "\\(\\frac{2}{\\sqrt{5}}\\), \\(\\frac{3}{5}\\), \\(\\frac{4}{5\\sqrt{5}}\\), \\(\\frac{5}{25}\\)",
            "11\\(\\frac{1}{9}\\), 12\\(\\frac{1}{2}\\), 14\\(\\frac{2}{7}\\), 16\\(\\frac{2}{3}\\)",
            "(2, 3), (3, 5), (5, 7), (7, 11), (11, 13), (.....)"
        ],
        "from": 1,
    }
]

# def parse_options_file() -> list[list[str]]:
#     with open("./reasoning/series-completion/options/3a.txt") as exercise_txt:
#         file_contents: str = exercise_txt.read()
#     return [group.split("\n") for group in file_contents.split("\n\n")]


# PARENT_QUESTION: str = "Directions : In each of the following questions, a number series is given with one term missing. Choose the correct alternative that will continue the same pattern and fill in the blank spaces."
# with open("./reasoning/series-completion/blanks.txt") as blanks_txt:
#     blank_questions: list[str] = [line.strip() for line in blanks_txt.readlines()]
# ungrouped_questions: list[str] = [
#     "In the series 10, 17, 24, 31, 38, ..., which of the following will be a number in the series ?",
#     "Which of the following will not be a number of the series 1, 8, 27, 64, 125, ..., ?",
#     "In the series 3, 9, 15, ..., what will be the 21st term ?",
#     "In the series 2, 6, 18, 54, ..., what will be the 8th term ?",
#     "Which term of the series 5, 8, 11, 14, ... is 320 ?",
#     "Which term of the series 5, 10, 20, 40, ... is 1280 ?"
# ]

# options: list[list[str]] = parse_options_file()

CORRECT_OPTIONS: list[str] = [
    "b",
    "c",
    "b",
    "c",
    "c",
    "b",
    "a",
    "a",
    "b",
    "c",
    "d",
    "c",
    "d",
    "c",
    "a",
    "d",
    "b",
    "d",
    "d",
    "c",
    "a",
    "a",
    "d",
    "c",
    "d",
    "c",
    "c",
    "d",
    "b",
    "b",
    "d",
    "b",
    "b",
    "c",
    "d",
    "b",
    "d",
    "d",
    "c",
    "a",
    "c",
    "c",
    "a",
    "a",
    "a",
    "b",
    "a",
    "b",
    "d",
    "d",
    "b",
    "c",
    "b",
    "a",
    "a",
    "b",
    "a",
    "b",
    "a",
    "a",
    "c",
    "b",
    "d",
    "a",
    "a",
    "a",
    "d",
    "b",
    "b",
    "d",
    "c",
    "b",
    "a",
    "c",
    "b",
    "c",
    "b",
]

# blank_questions_model: list[Question] = []
# for idx in range(len(blank_questions)):
#     blank_questions_model.append(
#         Question(
#             question=blank_questions[idx],
#             options=options[idx],
#             correct_option=answers[idx],
#         )
#     )

# group: Group = Group(parent_question=PARENT_QUESTION, questions=blank_questions_model)

# exercise: list[Group | Question] = []
# exercise.append(group)
# for idx in range(len(ungrouped_questions)):
#     question: Question = Question(
#         question=ungrouped_questions[idx],
#         options=options[-6 + idx],
#         correct_option=answers[-6 + idx],
#     )
#     exercise.append(question)

# with open("./reasoning/series-completion/3a.json", "w") as three_a_json:
#     json.dump([model.model_dump() for model in exercise], three_a_json, indent=2)
