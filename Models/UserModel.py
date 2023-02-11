from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    ForeignKeyConstraint,
    String,
)
from sqlalchemy.orm import relationship

from Models.BaseModel import EntityMeta

class User(EntityMeta):
    __tablename__ = "user"

    id = Column(Integer)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    photo_url = Column(String)

    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "name": self.name.__str__(),
        }