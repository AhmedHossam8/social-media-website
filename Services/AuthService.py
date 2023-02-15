from typing import List, Optional
import uuid

from fastapi import Depends
from Models.UserModel import User

from Repositories.UserRepository import UserRepository


class AuthService:
    userRepository: UserRepository

    def __init__(
        self, userRepository: UserRepository = Depends()
    ) -> None:
        self.userRepository = userRepository


    def login(
        self,
        email: str,
        password: str
    ):
        user = self.userRepository.get_by_email(email)

        if not user:
            return False

        return password == user.password


    def signUp(
        self,
        name: str,
        email: str,
        password: str
    ):
        user = User(
            id=uuid.uuid4(),
            name=name,
            email=email,
            password=password
        )

        user = self.userRepository.get_by_email(email=email)
        
        if user:
            print("User Already Exists")
            return False
        
        user = self.userRepository.create(user)
        return False if user is None else True

    