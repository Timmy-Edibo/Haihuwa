from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from .. import  models
from ..schemas import UsersForm, InsuranceForm, QRPAgentForm
from ..database import SessionLocal, engine
from sqlalchemy.exc import IntegrityError

router = APIRouter(tags=['Users'])

from ..utils import hash

models.Base.metadata.create_all(bind=engine)

from fastapi.middleware.cors import CORSMiddleware


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def home():
    return "Hello World"

#######################################################################################################

@router.get("/users")
def users(db: Session = Depends(get_db)):
    return db.query(models.Users).all()


@router.post("/users")
def users(user_form: UsersForm, db: Session = Depends(get_db)):
    try:
        hashed_password = hash(user_form.hashed_password)
        user_form.hashed_password = hashed_password

        query = models.Users(**user_form.__dict__)
        db.add(query)
        db.commit()
        db.refresh(query)
    except IntegrityError as e:

        db.rollback()
        if "UNIQUE constraint failed: users.email" in str(e):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
            detail="email address already exisy in database") from e

        elif " UNIQUE constraint failed: users.username" in str(e):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
            detail="username address already exisy in database") from e

        else: raise e    

    return query




@router.get("/insurance")
def users(db: Session = Depends(get_db)):
    return db.query(models.Insurance).all()


@router.post("/insurance")
def insurance(user_form: InsuranceForm, db: Session = Depends(get_db)):
    try:
        query = models.Insurance(**user_form.__dict__)
        db.add(query)
        db.commit()
        db.refresh(query)
    except IntegrityError as e:

        db.rollback()
        if "UNIQUE constraint failed: users.email" in str(e):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
            detail="email address already exisy in database") from e

        elif " UNIQUE constraint failed: users.username" in str(e):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
            detail="username address already exisy in database") from e

        else: raise e    

    return query



@router.get("/qrp_agents")
def qrp_agents(db: Session = Depends(get_db)):
    return db.query(models.QRPAgent).all()


@router.post("/qrp_agents")
def qrp_agents(user_form: QRPAgentForm, db: Session = Depends(get_db)):
    try:
        query = models.QRPAgent(**user_form.__dict__)
        db.add(query)
        db.commit()
        db.refresh(query)
    except IntegrityError as e:

        db.rollback()
        if "UNIQUE constraint failed: users.email" in str(e):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
            detail="email address already exisy in database") from e

        elif " UNIQUE constraint failed: users.username" in str(e):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
            detail="username address already exisy in database") from e

        else: raise e    

    return query


