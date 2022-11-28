from pydantic import BaseModel, EmailStr


class NewUserSchema(BaseModel):
    username: str
    email: str
    password: str


class RegistrationUserSchema(NewUserSchema):
    username: str
    email: str
    password: str
    repeat_password: str


class LoginUserSchema(BaseModel):
    email: str
    password: str


class PublicUserSchema(BaseModel):
    username: str
    email: str


class AccessRefreshTokenSchema(BaseModel):
    access: str
    refresh: str = None
