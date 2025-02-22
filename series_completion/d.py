# import json

from typing import Any

# from model.Reasoning import Group, Question


QUESTIONS: Any = [
    {
        "parent_question": "Directions : In each of the following letter series, some of the letters are missing which are given in that order as one of the alternatives below it. Choose the correct alternative.",
        "questions": [
            "_ _ aba _ _ ba _ ab",
            "ab _ _ _ b _ bbaa _",
            "_ baa _ aab _ a _ a",
            "_ _ babbba _ a _ _",
            "aa _ ab _ _ aaa _ a",
            "a _ bbc _ aab _ cca _ bbcc",
            "ab _ aa _ bbb _ aaa _ bbba",
            "bc _ b _ c _ b _ ccb",
            "abb _ baa _ a _ bab _ aba",
            "abca _ bcaab _ ca _ bbc _ a",
            "_ bbca _ bcca _ ac _ a _ cb",
            "_ bcc _ ac _ aabb _ ab _ cc",
            "a _ bccb _ ca _ cca _ baab _ c",
            "ab _ aa _ caab_ c _ abb _ c",
            "c _ baa _ aca _ cacab _ acac _ bca",
            "_ aba _ cabc _ dcba _ bab _ a",
            "a _ cdaab _ cc _ daa _ bbb _ ccddd",
            "a _ abbb _ ccccd _ ddccc _ bb _ ba",
            "_ bcdbc _ dcabd _ bcdbc _ dc _ bd",
            "adb _ ac _ da _ cddcb _ dbc _ cbda",
            "c _ bbb _ _ abbbb _ abbb _",
            "b _ abbc _ bbca _ bcabb _ ab",
            "ac _ cab _ baca _ aba _ acac",
            "_ acca _ ccca _ acccc _ aaa",
            "_ bc _ _ bb _ aabc",
            "aa _ aaa _ aaaa _ aaaa _ b",
            "aba _ baca _ ba _ baccaabac _ aca",
            "ab _ bc _ c _ ba _ c",
            "a _ ca _ bc _ bcc _ bca",
            "ab _ bcbca _ _ c _ bab",
            "a _ cacbc _ baca _ _ b",
            "_ aaba _ bba _ bba _ abaa _ b",
            "ab _ bbc _ c _ ab _ ab _ b",
            "_ bca _ cca _ ca _ b _ c",
            "b _ ac _ cc _ cb _ ab _ ac",
            "c _ ac _ aa _ aa _ bc _ bcc",
            "abc _ d _ bc _ d _ b _ cda",
            "ba _ b _ aab _ a _ b",
            "gfe _ ig _ eii _ fei _ gf _ ii",
            "mnonopqopqrs _ _ _ _ _",
            "aab _ ab _ cabcca _ bcab _ c",
            "ccbab _ caa _ bccc _ a _",
            "ba _ b _ aabb _ a _ _ a _ bb",
            "a _ c _ abb _ a _ bc _ bc _ ab",
            "cab _ a _ c _ bc _ bc _ b _ ab",
            "cccbb _ aa _ cc _ bbbaa _ c",
            "_ abb _ _ bb _ a _ bbab _ ba",
            "ccb _ c _ bbc _ b _ cc _ _ ccbb",
            "abca _ bcaab _ aa _ caa _ c",
            "b _ b _ bb _ _ bbb _ bb _ b",
            "c _ bba _ cab _ ac _ ab _ ac",
            "a _ bc _ c _ abb _ bca _",
            "_ c _ bd _ cbcda _ a _ db _ a",
            "a _ bc _ a _ bcda _ ccd _ bcd _",
            "_ cb _ ca _ bacb _ ca _ bac _ d",
        ],
        "from": 1
    },
    {
        "parent_question": "Directions : In each of the followsing number questions, three sequences of letters/numerals are given which correspond to each other other in some way. In each question, you have to find out the letters/numerals that come in the vacant places marked by (?). These are given as one of the four alternatives under the question. Mark your answer as instructed.",
        "questions": [
            "C B _ _ D _ B A B C C B<br>_ _ 1 2 4 3 _ _ ? ? ? ?<br>a _ a b _ c _ b _ _ _ _",
            "_ A C _ B D _ C D C D<br>2 _ 4 1 _ 1 4 _ _ _ _<br>c d _ b c _ a ? ? ? ?",
            "C _ B _ D _ A _ B B D D<br>2 _ _ 4 _ 3 4 _ ? ? ? ?<br>_ a _ c b a _ d _ _ _ _",
            "A _ B A C _ D _ B C D C<br>_ 3 _ 2 _ 1 _ 4 ? ? ? ?<br>d c _ _ b a c b _ _ _ _",
            "_ A D A C B _ _ B D C C<br>1 3 _ _ 1 2 4 2 _ _ _ _<br>a _ _ b _ _ c d ? ? ? ?"
        ],
        "from": 56
    }
]


# def parse_options_file() -> list[list[str]]:
#     with open("./reasoning/series-completion/options/3d.txt") as options_txt:
#         file_contents: str = options_txt.read()
#     options: list[list[str]] = [group.split("\n") for group in file_contents.split("\n\n")]
#     assert not options[-1][-1]
#     del options[-1][-1]
#     return options

CORRECT_OPTIONS: list[str] = [
    "b",
    "c",
    "c",
    "d",
    "a",
    "b",
    "b",
    "a",
    "a",
    "c",
    "b",
    "c",
    "a",
    "d",
    "a",
    "a",
    "d",
    "c",
    "a",
    "b",
    "b",
    "c",
    "a",
    "b",
    "a",
    "d",
    "a",
    "c",
    "a",
    "d",
    "b",
    "a",
    "c",
    "b",
    "d",
    "b",
    "c",
    "b",
    "c",
    "c",
    "d",
    "a",
    "b",
    "c",
    "d",
    "b",
    "b",
    "a",
    "c",
    "c",
    "b",
    "c",
    "a",
    "b",
    "c",
    "c",
    "a",
    "d",
    "b",
    "d"
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


# with open("./reasoning/series-completion/3d.json", "w") as three_b_json:
#     json.dump(
#         [model.model_dump() for model in exercises],
#         three_b_json,
#         indent=2,
#     )
