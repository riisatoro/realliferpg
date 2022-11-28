from auth.dependencies import check_password, create_jwt, make_password
from auth.schemas import (
    AccessRefreshTokenSchema,
    LoginUserSchema,
    NewUserSchema,
    PublicUserSchema,
    RegistrationUserSchema,
)
from db.collections import User
from db.queries import count_existed_in_db, find_in_db, save_to_db
from fastapi import APIRouter

router = APIRouter(tags=["Auth"])


@router.post("/registration")
def registration(new_user: RegistrationUserSchema) -> PublicUserSchema:
    users_amount = count_existed_in_db(
        User, username=new_user.username, email=new_user.email
    )
    if users_amount:
        raise ValueError("Can't create a user.")

    new_user_values = {**new_user.dict(), "password": make_password(new_user.password)}
    new_user = NewUserSchema(**new_user_values)

    save_to_db(User, new_user.dict())
    return PublicUserSchema(**new_user.dict()).dict()


@router.post("/login")
def login(user: LoginUserSchema) -> AccessRefreshTokenSchema:
    existed_user = find_in_db(User, email=user.email)
    if len(existed_user) != 1:
        raise ValueError("Can't log in this user.")

    existed_user = existed_user[0]
    if not check_password(user.password, existed_user["password"]):
        raise ValueError("Invalid password.")

    tokens = AccessRefreshTokenSchema(
        access=create_jwt(existed_user["email"]), refresh=None
    )
    return tokens.dict()
