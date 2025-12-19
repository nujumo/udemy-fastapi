from datetime import timedelta, datetime, timezone
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from ..database import SessionLocal
from ..models import Users
from passlib.context import CryptContext
from jose import jwt, JWTError
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

SECRET_KEY = 'da616b0c61137802ec20d6701cd1f45815285c3996b28cb250e74a5a6fb22499'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str
    phone_number: str

class Token(BaseModel):
    access_token: str
    token_type: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

templates = Jinja2Templates(directory="ToDoApp/templates")

### Pages ###
@router.get('/login-page')
def render_login_page(request: Request):
    return templates.TemplateResponse('login.html', {"request": request})

@router.get('/register-page')
def render_register_page(request: Request):
    return templates.TemplateResponse('register.html', {"request": request})

### Endpoints ###
def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id: int, role:str, expires_delta: timedelta):
    encode = {
        'sub': username,
        'id': user_id,
        'role': role,
    }
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        user_role: str = payload.get('role')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not validate user.')
        return {'username': username, 'id': user_id, 'user_role': user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate user.')
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency,
                      create_user_request: CreateUserRequest):
    create_user_model = Users(
        username=create_user_request.username,
        email=create_user_request.email,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True,
        phone_number=create_user_request.phone_number,
    )

    db.add(create_user_model)
    db.commit()

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate user.')
    token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))
    return {'access_token':token, 'token_type':'bearer'}

"""
What is a JSON Web Token?
=========================
- JSON Web Token (JWT) is a self-contained way to securely transmit data and information between two parties using a JSON object
- JSON Web Tokens can be trusted because each JWT can be digitally signed, which in return allows the server to know if the JWT has been changed at all
- JWT should be used when dealing with authorization
- JWT is a great way for information to be exchanged between the server and client

JSON Web Token Structure
========================
- A JSON Web Token is created of three separate parts separated by dots (.) which include:
    - Header: (a)
    - Payload: (b)
    - Signature: (c)

    e.g. aaaaaaaaa.bbbbbbbb.ccccccccc
    
JWT Header
==========
- A JWT header usually consists of two parts:
    - (alg) The algorithm for signing
    - "typ" The specific type of token
 - The JWT header is then encoded using Base64 to create the first part of the JWT (a).
   
    e.g. {
        "alg": "HS256",
        "typ": "JWT",
    }

JWT Payload
===========
- A JWT Payload consists of the data. The Payload data contains claims, and there are three different types of claims.
    - Registered (iss, sub, exp)
    - Public
    - Private
- The JWT Payload is then encoded using Base64 to create the second part of the JWT (b).
    e.g. {
        "sub": 1234567890,
        "name": 'Nuala Mo',
        "given_name": 'Nuala',
        "family_name": 'Mo',
        "email": 'nujumo@email.com',
        "admin:" true
    }

JWT Signature
=============
- A JWT Signature is created by using the algorithm in the header to hash out the encoded header, encoded payload with a secret
- The secret can be any, but is saved somewhere on the server that the client does not have access to
- The signature is the third and final part of a JWT (c).

    e.g. 
    HMACSHA256(
        base64URLEncode(header) + "." +
        base64URLEncode(payload),
        secret)
"""