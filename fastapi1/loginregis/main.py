from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session
import database, models_and_schemas, crud, auth
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

@app.on_event("startup")
def startup_event():
    database.create_db_and_tables()

@app.on_event("shutdown")
def shutdown_event():
    database.shutdown()

@app.post("/register")
def register_user(user: models_and_schemas.UserSchema, db: Session = Depends(database.get_db)):
    db_user = crud.create_user(db = db, user = user)
    return db_user

@app.post("/login")
def login(db: Session = Depends(database.get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    db_user = crud.get_user_by_username(db = db, username = form_data.username)
    if not db_user:
        raise HTTPException(status_code = 401, detail = "Username tidak ditemukan")
    if auth.verify_password(form_data.password, db_user.hashed_password):
        token = auth.create_access_token(db_user)
        return {"access_token": token, "token_type": "Bearer"}
    raise HTTPException(status_code = 401, detail = "Password salah")

@app.get('/users')
def get_all_users(db: Session = Depends(database.get_db)):
    users = crud.get_users(db = db)
    return users

@app.get('/secured', dependencies = [Depends(auth.check_active)])
def get_all_users(db: Session = Depends(database.get_db)):
#def get_all_users(db: Session = Depends(database.get_db), active: bool = Depends(auth.check_active)):
    users = crud.get_users(db = db)
    return users

@app.get('/adminsonly', dependencies = [Depends(auth.check_admin)])
def get_all_users(db: Session = Depends(database.get_db)):
    users = crud.get_users(db = db)
    return users
