import datetime

from pydantic import BaseModel, EmailStr, field_validator


class BaseUser(BaseModel):
    name: str
    username: str
    email: EmailStr

    @field_validator("name", "surname", check_fields=False)
    def name_contain_space(cls, v):
        if " " in v:
            raise ValueError("Name or surname contain space")
        return v

    @field_validator("name", "surname", check_fields=False)
    def name_contain_numeric(cls, v):
        if not v.isalpha:
            raise ValueError("Name or surname contains numbers")
        return v

class UserInDB(BaseUser):
    hashed_password: str
    is_active: int


class UserIn(BaseUser):
    password: str


class UserOut(BaseUser):
    id: int
    created_at: datetime.datetime
    is_active: int