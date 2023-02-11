from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session, lazyload

from Configs.Database import (
    get_db_connection,
)
from Models.PostModel import Post

class PostRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db


    def get(self, post: Post) -> Post:
        return self.db.get(
            Post,
            post.id
        )