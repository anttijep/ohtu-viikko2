from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if len(username) < 3:
            raise UserInputError("Username should have at least 3 characters")

        if len(password) < 8:
            raise UserInputError("Password should have at least 8 characters")

        if not username.isalpha() or not username.islower():
            raise UserInputError("Username can only contain letters a-z")

        if self._user_repository.find_by_username(username) is not None:
            raise UserInputError("Username already in use")

        if password.isalpha():
            raise UserInputError("Password should contain at least one non-letter character")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
