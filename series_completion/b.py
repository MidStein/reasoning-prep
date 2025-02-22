# import json

from typing import Any
# from model.Reasoning import Group, Question

QUESTIONS: Any = [
    {
        "parent_question": "Directions : In each of the following questions, one term in the number series is wrong. Find out the wrong term.",
        "questions": [
            "24, 27, 31, 33, 36",
            "196, 169, 144, 121, 80",
            "3, 5, 7, 9, 11, 13",
            "121, 143, 165, 186, 209",
            "1, 2, 4, 8, 16, 32, 64, 96",
            "8, 14, 26, 48, 98, 194, 386",
            "8, 13, 21, 32, 47, 63, 83",
            "3, 10, 27, 4, 16, 64, 5, 25, 125",
            "380, 188, 92, 48, 20, 8, 2",
            "1, 3, 7, 15, 27, 63, 127",
            "5, 10, 17, 24, 37",
            "1, 3, 10, 21, 64, 129, 256, 778",
            "15, 16, 22, 29, 45, 70",
            "6, 14, 30, 64, 126",
            "10, 26, 74, 218, 654, 1946, 5834",
            "3, 7, 15, 39, 63, 127, 255, 511",
            "445, 221, 109, 46, 25, 11, 4",
            "1236, 2346, 3456, 4566, 5686",
            "5, 10, 40, 80, 320, 550, 2560",
            "3, 2, 8, 9, 13, 22, 18, 32, 23, 42",
            "8, 27, 125, 343, 1331",
            "10, 14, 28, 32, 64, 68, 132",
            "1, 5, 5, 9, 7, 11, 11, 15, 12, 17",
            "11, 2, 21, 3, 32, 4, 41, 5, 51, 6",
            "11, 5, 20, 12, 40, 26, 74, 54",
            "56, 72, 90, 110, 132, 150",
            "8, 13, 21, 32, 47, 63, 83",
            "89, 78, 86, 80, 85, 82, 83",
            "25, 36, 49, 81, 121, 169, 225",
            "2, 5, 10, 17, 26, 37, 50, 64",
            "1, 5, 9, 16, 25, 37, 49,",
            "2, 5, 10, 50, 500, 5000",
            "46080, 3840, 384, 48, 24, 2, 1",
            "105, 85, 60, 30, 0, -45, -90,",
            "325, 259, 202, 160, 127, 105, 94",
            "125, 126, 124, 127, 123, 129",
            "3, 4, 10, 32, 136, 685, 4116",
            "3, 10, 27, 4, 16, 64, 5, 25, 125",
            "5, 27, 61, 122, 213, 340, 509",
            "16, 22, 30, 45, 52, 66",
        ],
        "from": 1,
    },
    {
        "parent_question": "Directions : In each of the following number series, either one term is missing or is wrong which has been given as one of the four alternatives under it. This alternative is your answer.",
        "questions": [
            "1, 2, 5, 10, 17, 28",
            "1, 5, 11, 19, 29, 55",
            "2, 3, 5, 8, 13, 34",
            "0, 3, 8, 15, 24, 33",
            "1, 5, 14, 30, 55, 93",
        ],
        "from": 41,
    },
    {
        "parent_question": "Directions : In each of the followsing number series, two terms have been put within brackets. Mark your answer as<br>(a) if both the bracketed terms are right;<br>(b) if the first bracketed term is right and second is wrong;<br>(c) if the first bracketed term is wrong and second is right;<br>(d) if both the bracketed terms are wrong.",
        "questions": [
            "4, 6, 10, (12), 16, (14), 22",
            "3, 10, 29, (66), (127), 218,",
            "2, 3, (6), 11, 18, (30), 38",
            "(2), 5, (12), 25, 41, 61",
            "4, 7, (9), 10, 13, 15, (16), 19",
        ],
        "from": 46,
        "no_options": True
    },
]


# def parse_options_file() -> List[List[str]]:
#     with open("./reasoning/series-completion/options/3b.txt") as options_txt:
#         file_contents: str = options_txt.read()
#     options: List[List[str]] = [
#         group.split("\n") for group in file_contents.split("\n\n")
#     ]
#     assert not options[-1][-1]
#     del(options[-1][-1])
#     return options


# options: List[List[str]] = parse_options_file()

CORRECT_OPTIONS: list[str] = [
    "c",
    "a",
    "d",
    "c",
    "d",
    "b",
    "d",
    "c",
    "c",
    "c",
    "c",
    "d",
    "b",
    "c",
    "d",
    "b",
    "b",
    "d",
    "c",
    "b",
    "d",
    "d",
    "b",
    "c",
    "c",
    "d",
    "c",
    "c",
    "a",
    "d",
    "b",
    "d",
    "c",
    "c",
    "c",
    "d",
    "b",
    "c",
    "a",
    "b",
    "b",
    "b",
    "a",
    "d",
    "c",
    "b",
    "a",
    "b",
    "d",
    "a",
]

# case: List[Group | Question] = []
# for item in QUESTIONS:
#     if not isinstance(item, str):
#         questions: List[Question] = []
#         for idx in range(len(item["questions"])):
#             try:
#                 if item["from"] == 46:
#                     question: Question = Question(
#                         question=item["questions"][idx],
#                         options=None,
#                         correct_option=answers[item["from"] - 1 + idx]
#                     )
#                 else:
#                     question: Question = Question(
#                         question=item["questions"][idx],
#                         options=options[item["from"] - 1 + idx],
#                         correct_option=answers[item["from"] - 1 + idx],
#                     )
#                 questions.append(question)
#             except IndexError as e:
#                 print(item["from"])
#                 print(idx)
#                 raise (e)
#         group: Group = Group(
#             parent_question=item["parent_question"], questions=questions
#         )
#         case.append(group)

# with open("./reasoning/series-completion/3b.json", "w") as three_b_json:
#     json.dump([model.model_dump() for model in case], three_b_json, indent=2)
