"""
Create
Read
Update
Delete
"""

from users.shemas import CreateUser


def create_user(user_in: CreateUser) -> dict:
    user = user_in.model_dump()  # повертає словник
    return {
        "success": True,
        "user": user,
    }
