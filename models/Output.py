from pydantic import BaseModel

class Question(BaseModel):
    question: str
    options: list[str] | None
    correct_option: str


class Group(BaseModel):
    parent_question: str
    questions: list[Question]


# class Example(BaseModel):
#     question: str
#     options: list[str]
#     correct_option: str


class Case(BaseModel):
    case_name: str | None = None
    # examples: list[Example]
    items: list[Group | Question]


class Type(BaseModel):
    type_name: str
    cases: list[Case]


class Chapter(BaseModel):
    chapter_name: str
    types: list[Type]
