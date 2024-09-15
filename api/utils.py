from fastapi import HTTPException
from passlib.context import CryptContext 
from starlette import status
class PasswordHashing:
    def __init__(self) -> None:
        self.pwd_context = CryptContext(schemes= ["bcrypt"], deprecated= "auto")
    

    def hash_password(self, password: str):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str):
        try:
            return self.pwd_context.verify(plain_password, hashed_password)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Password verification failed: {str(e)}")
