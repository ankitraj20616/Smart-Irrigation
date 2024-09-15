from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from config import settings
from collections.abc import Mapping
class JWT_Auth:
    def __init__(self) -> None:
        self.SECRET_KEY = settings.SECRET_KEY
        self.ALGORITHM = settings.ALGORITHM
        self.ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
    
    def create_access_token(self, data: dict, expires_delta: timedelta = None):
        data_to_encode = data.copy()
        if expires_delta:
            expire_time = datetime.now(timezone.utc) + expires_delta
        else:
            expire_time = datetime.now(timezone.utc) + timedelta(minutes= self.ACCESS_TOKEN_EXPIRE_MINUTES)
        
        data_to_encode.update({"exp": expire_time})
        encoded_jwt = jwt.encode(data_to_encode, self.SECRET_KEY, algorithm= self.ALGORITHM)
        return encoded_jwt


    def verify_token(self, token: str):
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms= [self.ALGORITHM])
            phone_no: str = payload.get("phone_no")
            if phone_no is None:
                raise JWTError
            return phone_no
        except JWTError:
            return None
