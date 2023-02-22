"""
Utils for hashing content
"""
from passlib.context import CryptContext

pwd_ctxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

class HashPwd():
    """Hashing and Verifying Passwords"""
    def bcrypt(password: str):
        return pwd_ctxt.hash(password)

    def verify(test_pass, hashed_pass):
        return pwd_ctxt.verify(test_pass, hashed_pass)