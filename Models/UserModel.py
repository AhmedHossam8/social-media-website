from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String
)

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
            "email": self.email.__str__(),
            "photo_url": self.photo_url.__str__()
        }