from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    ForeignKeyConstraint,
    String,
)
from sqlalchemy.orm import relationship

from Models.BaseModel import EntityMeta
from Models.UserModel import User

class Post(EntityMeta):
    __tablename__ = "post"

    id = Column(Integer)
    body = Column(String, nullable=False)
    user_id = Column(String, nullable=False)

    PrimaryKeyConstraint(id)
    # ForeignKeyConstraint(user_id, User.id)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "body": self.body.__str__(),
        }