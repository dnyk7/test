from backend import crud
from backend import models
from backend import schemas
from backend.database import SessionLocal, engine

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Remove or modify catch_all_get endpoint
# Only uncomment if you specifically need this for other purposes
# @app.api_route("/{path_name:path}", methods=["GET"])
# async def catch_all_get(req: Request, path_name: str):
#     raise HTTPException(status_code=403, detail="User sent a GET Request")

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_id(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user

# By fren
# @app.post("/accounts/", response_model=schemas.Account)
# def create_account(account: schemas.AccountCreate, user_id: int, db: Session = Depends(get_db)):
#     return crud.create_account(db=db, account=account, user_id=user_id)

@app.post("/transactions/", response_model=schemas.Transaction)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db=db, transaction=transaction)

@app.get("/users/", response_model=list[schemas.User])
def read_all_users(skip: int = 0, limit=None, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users