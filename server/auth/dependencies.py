import os
import time

import jwt
from bcrypt import checkpw, gensalt, hashpw

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_EXPIRES_AT = int(os.getenv("JWT_EXPIRES_AT"))
JWT_ALGORITHM = "HS256"


def make_password(password):
    return hashpw(password.encode(), gensalt())


def check_password(password, hashed_password):
    return checkpw(password.encode(), hashed_password.encode())


def create_jwt(userID: str):
    payload = {"userID": userID, "expire": time.time() + JWT_EXPIRES_AT}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_jwt(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        if decoded_token["expires"] >= time.time():
            return decoded_token
        raise ValueError()
    except:
        return None
