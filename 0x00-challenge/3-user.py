#!/usr/bin/python3
"""
User Model
"""
import hashlib
import uuid


class User:
    """
    User class:
    - id: public string unique (uuid)
    - password: private string hash in MD5
    """

    def __init__(self):
        """
        Initialize a new user:
        - assigned a unique `id`
        """
        self.id = str(uuid.uuid4())
        self.__password = None  # Initialize __password here

    @property
    def password(self):
        """
        Password getter
        """
        return self.__password

    @password.setter
    def password(self, pwd):
        """
        Password setter:
        - `None` if `pwd` is `None`
        - `None` if `pwd` is not a string
        - Hash `pwd` in MD5 before assigning to `__password`
        """
        if pwd is None or not isinstance(pwd, str):  # Use isinstance for type checking
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd):
        """
        Valid password:
        - `False` if `pwd` is `None`
        - `False` if `pwd` is not a string
        - `False` if `__password` is `None`
        - Compare `__password` and the MD5 value of `pwd`
        """
        if pwd is None or not isinstance(pwd, str):  # Use isinstance for type checking
            return False
        if self.__password is None:
            return False
        return hashlib.md5(pwd.encode()).hexdigest() == self.__password  # Compare in lowercase

if __name__ == '__main__':
    print("Test User")

    user_1 = User()
    assert user_1.id is not None, "New User should have an id"  # Use assert for validation

    user_2 = User()
    assert user_1.id != user_2.id, "User.id should be unique"  # Use assert for validation

    u_pwd = "myPassword"
    user_1.password = u_pwd
    assert user_1.password != u_pwd, "User.password should be hashed"  # Use assert for validation

    assert user_2.password is None, "User.password should be None by default"  # Use assert for validation

    user_2.password = None
    assert user_2.password is None, "User.password should be None if set to None"  # Use assert for validation

    user_2.password = "89"  # Set as string
    assert user_2.password is not None, "User.password should be None if set to a non-string"  # Use assert for validation

    assert user_1.is_valid_password(u_pwd), "is_valid_password should return True if it's the right password"  # Use assert for validation

    assert not user_1.is_valid_password("Fakepwd"), "is_valid_password should return False if it's not the right password"  # Use assert for validation

    assert not user_1.is_valid_password(None), "is_valid_password should return False if compared with None"  # Use assert for validation

    assert not user_1.is_valid_password(89), "is_valid_password should return False if compared with an integer"  # Use assert for validation

    assert not user_2.is_valid_password("No pwd"), "is_valid_password should return False if no password is set before"  # Use assert for validation
