import json

from models.Output import Chapter, Question


def load_data_model() -> list[Chapter]:
    with open("data.json") as data_json:
        chapters_json = json.load(data_json)
    return [Chapter(**chapter) for chapter in chapters_json]


def get_transformed(chapter: Chapter) -> list[Question]:
    questions: list[Question] = []
    for problem_type in chapter.types:
        for case in problem_type.cases:
            for item in case.items:
                if isinstance(item, Question):
                    questions.append(item)
                else:
                    questions.extend(
                        [
                            Question(
                                question=item.parent_question
                                + "\n\n"
                                + question.question,
                                options=question.options,
                                correct_option=question.correct_option,
                            )
                            for question in item.questions
                        ]
                    )
    return questions


def main():
    chapters: list[Chapter] = load_data_model()
    questions: list[Question] = get_transformed(chapters[0])
    with open("transformed-data.json", "w") as transformed_data_json:
        json.dump(
            [question.model_dump() for question in questions],
            transformed_data_json,
            indent=2,
        )


if __name__ == "__main__":
    main()
