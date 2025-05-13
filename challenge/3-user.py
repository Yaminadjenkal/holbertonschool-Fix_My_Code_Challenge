#!/usr/bin/python3
"""
User Model - Secure Version
"""
import hashlib
import uuid


class User:
    """
    User class:
    - id: unique public string (UUID)
    - password: private string hashed securely
    """

    def __init__(self):
        """Initialize a new user with a unique `id`."""
        self.id = str(uuid.uuid4())
        self.__password = None  # Mot de passe privé

    @property
    def password(self):
        """Password getter - Returns hashed password."""
        return self.__password

    @password.setter
    def password(self, pwd):
        """
        Password setter:
        - Sets password to None if `pwd` is invalid (None or non-string)
        - Hashes `pwd` securely using SHA-256 before storing
        """
        if not isinstance(pwd, str) or pwd is None:
            self.__password = None
        else:
            self.__password = hashlib.sha256(pwd.encode()).hexdigest()

    def is_valid_password(self, pwd):
        """
        Validates a password:
        - Returns False if `pwd` is None or not a string
        - Returns False if no password has been set
        - Compares stored hashed password with hashed input password
        """
        if not isinstance(pwd, str) or pwd is None or self.__password is None:
            return False
        return hashlib.sha256(pwd.encode()).hexdigest() == self.__password


# Testing the User class
if __name__ == "__main__":
    print("Test User")

    user_1 = User()
    if user_1.id is None:
        print("New User should have an id")

    user_2 = User()
    if user_1.id == user_2.id:
        print("User.id should be unique")

    u_pwd = "mySecurePassword"
    user_1.password = u_pwd
    if user_1.password == u_pwd:
        print("User.password should be hashed")

    if user_2.password is not None:
        print("User.password should be None by default")

    user_2.password = None
    if user_2.password is not None:
        print("User.password should be None if set to None")

    user_2.password = 89
    if user_2.password is not None:
        print("User.password should be None if set to an integer")

    if not user_1.is_valid_password(u_pwd):
        print("is_valid_password should return True for correct password")

    if user_1.is_valid_password("Fakepwd"):
        print("is_valid_password should return False for incorrect password")

    if user_1.is_valid_password(None):
        print("is_valid_password should return False for None password")

    if user_1.is_valid_password(89):
        print("is_valid_password should return False for integer password")

    if user_2.is_valid_password("No pwd"):
        print("is_valid_password should return False if no password was set")
