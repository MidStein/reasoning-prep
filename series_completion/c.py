# import json

from typing import Any
# from model.Reasoning import Group, Question


QUESTIONS: Any = [
    {
        "parent_question": "Directions : In each of the following questions, various terms of a letter series are given with one term missing as shows by (?). Choose the missing term out of the given alternatives.",
        "questions": [
            "U, O, I, ?, A",
            "Y, W, U, S, Q, ?, ?",
            "A, B, D, G, ?",
            "Z, U, Q, ?, L",
            "A, C, F, H, ?, M",
            "A, Z, X, B, V, T, C, R, ?, ?",
            "R, M, ?, F, D, ?",
            "Z, L, X, J, V, H, T, F, ?, ?",
            "Z, S, W, O, T, K, Q, G, ?, ?",
            "W, V, T, S, Q, P, N, M, ?, ?",
            "Z, Y, X, U, T, S, P, O, N, K, ?, ?",
            "b e d f ? h j ? l",
            "AZ, BY, CX, ?",
            "AZ, CX, FU, ?",
            "AZ, GT, MN, ?, YB",
            "BF, CH, ?, HO, LT",
            "CE, GI, KM, OQ, ?",
            "BD, GI, LN, QS, ?",
            "AD, EH, IL, ?, QT",
            "JE, LH, OL, SQ, ?",
            "DF, GJ, KM, NQ, RT, ?",
            "CX FU, IR ? OL RI",
            "OTE, PUF, QVG, RWH, ?",
            "eac gce ieg ?",
            "ejo tyd ins xch ?",
            "CAT, FDW, IGZ, ?",
            "BEH, KNQ, TWZ, ?",
            "deb ijg nol ? xyv",
            "? siy oeu kaq gwm cri",
            "QPO, SRQ, UTS, WVU, ?",
            "? ayw gec mki sqo",
            "dfe jih mln ? vut",
            "DEF, HIJ, MNO, ?",
            "FLP, INS, LPV, ?",
            "shg rif qje pkd ?",
            "LXF, MTJ, NPN, OLR, ?",
            "MHZ, NIW, OKT, PNQ, ?",
            "AYD, BVF, DRH, ?, KGL",
            "AB, BA, ABC, CBA, ABCD, ?",
            "AB, DEF, HIJK, ?, STUVWX",
            "A, CD, GHI, ?, UVWXY",
        ],
        "from": 1
    },
    {
        "parent_question": "Directions : In each of the followsing number series, a sequence of groups of letters and numbers is given with one term missing as shown by (?). Choose the missing term out of the given alternatives.",
        "questions": [
            "D-4, F-6, H-8, J-10, ?, ?",
            "3F, 6G, 11I, 18L, ?",
            "KM5, IP8, GS11, EV14, ?",
            "J2Z, K4X, I7V, ?, H16R, M22P",
            "2Z5, 7Y7, 14X9, 23W11, 34V13, ?",
            "2A11, 4D13, 12G17, ?",
            "C4X, F9U, I16R, ?",
            "Q1F, S2E, U6D, W21C, ?"
        ],
        "from": 42
    },
    {
        "question": "Find the wrong term in the letter-number series given below :<br>G4T, J10R, M20P, P43N, S90L",
        "number": 50
    }
]

# def parse_options_file() -> list[list[str]]:
#     with open("./reasoning/series-completion/options/3c.txt") as options_txt:
#         file_contents: str = options_txt.read()
#     options: list[list[str]] = [group.split("\n") for group in file_contents.split("\n\n")]
#     assert not options[-1][-1]
#     del options[-1][-1]
#     return options

CORRECT_OPTIONS: list[str] = [
    "a",
    "e",
    "c",
    "d",
    "b",
    "a",
    "e",
    "a",
    "a",
    "d",
    "d",
    "a",
    "e",
    "c",
    "c",
    "c",
    "c",
    "e",
    "c",
    "e",
    "d",
    "a",
    "d",
    "c",
    "b",
    "d",
    "b",
    "d",
    "e",
    "c",
    "c",
    "c",
    "a",
    "a",
    "b",
    "a",
    "b",
    "b",
    "e",
    "a",
    "d",
    "c",
    "c",
    "e",
    "d",
    "b",
    "d",
    "c",
    "c",
    "b"
]

# options: list[list[str]] = parse_options_file()

# exercises: list[Group | Question] = []
# for item in QUESTIONS:
#     if "parent_question" in item:
#         assert isinstance(item, dict)
#         assert(isinstance(item["questions"], list))
#         questions: list[Question] = []
#         for idx in range(len(item["questions"])):
#             assert(isinstance(item["from"], int))
#             question: Question = Question(
#                 question=item["questions"][idx],
#                 options=options[item["from"] - 1 + idx],
#                 correct_option=correct_options[item["from"] - 1 + idx]
#             )
#             questions.append(question)
#         assert(isinstance(item["parent_question"], str))
#         exercises.append(Group(parent_question=item["parent_question"], questions=questions))
#     else:
#         question: Question = Question(
#             question=item["question"],
#             options=options[item["number"] - 1],
#             correct_option=correct_options[item["number"] - 1]
#         )
#         exercises.append(question)


# with open("./reasoning/series-completion/3d.json", "w") as three_b_json:
#     json.dump(
#         [model.model_dump() for model in exercises],
#         three_b_json,
#         indent=2,
#     )
