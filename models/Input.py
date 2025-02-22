from pydantic import BaseModel


class Group(BaseModel):
    parent_question: str
    questions: list[str]
    from_question: int
    no_options: bool = False


class Individual_Question(BaseModel):
    question: str
    number: int


class Case(BaseModel):
    case_name: str | None = None
    items: list[Group | Individual_Question]


class Type(BaseModel):
    type_name: str
    cases: list[Case]
