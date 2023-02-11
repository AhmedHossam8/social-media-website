from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session, lazyload

from Configs.Database import (
    get_db_connection,
)

from Models.UserModel import User
from Models.PostModel import Post

class UserRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db


    def get(self, user: User) -> User:
        return self.db.get(
            User,
            user.email,
            options=[lazyload(Post.body)],
        )

    def get_by_email(self, email: str) -> User:
        return self.db.get(
            User,
            email,
        )