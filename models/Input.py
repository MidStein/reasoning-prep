from pydantic import BaseModel


class Group(BaseModel):
    parent_question: str
    questions: list[str]
    from_question: int
    no_options: bool = False
    skip: bool = False
    modified: bool = False


class IndividualQuestion(BaseModel):
    question: str
    number: int
    modified: bool = False
    skip: bool = False


class Case(BaseModel):
    case_name: str | None = None
    items: list[Group | IndividualQuestion]
    skip: bool = False


class Type(BaseModel):
    type_name: str
    cases: list[Case]
