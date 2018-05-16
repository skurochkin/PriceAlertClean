import uuid

import src.models.users.errors as UserErrors
from src.common.utils import Utils
from src.common.database import Database


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        user_data = Database.find_one("users", {"email": email})
        if user_data is None:
            # Tell the user that e-mail doesn't exist
            raise UserErrors.UserNotExistsError("Your user does not exist.")

        if not Utils.check_hashed_passhword(password, user_data['password']):
            # Tell the user that their password is wrong
            raise UserErrors.IncorrectPasswordError("Your password was wrong.")

        return True