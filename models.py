from pydantic import BaseModel, field_validator, ValidationError, ValidationInfo
from datetime import datetime


class Student(BaseModel):
    name: str
    age: float
    year: float
    grade: float
    address: str
    father_name: str
    mother_name: str
    birthdate: str


    @field_validator('name')
    @classmethod
    def name_spaces(cls, v: str):
        if " " in v:
            return v.replace(" ", "_")
        return v

    @field_validator('father_name')
    @classmethod
    def father_name_spaces(cls, v: str):
        if " " in v:
            return v.replace(" ", "_")

    @field_validator('mother_name')
    @classmethod
    def mother_name_spaces(cls, v: str):
        if " " in v:
            return v.replace(" ", "_")


    @field_validator('birthdate')
    @classmethod
    def birthdate_date_str(cls, v: str):
        datetime.strptime(v, "%Y-%m-%d")
        return v

    @field_validator('age')
    @classmethod
    def age_validate(cls, v: float):
        return int(v)

    @field_validator('year')
    @classmethod
    def year_validate(cls, v: float):
        return int(v)
