from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import traceback

import models, schemas
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind = engine)
app = FastAPI(
    title = "BusinessCard API",
    description = "MVP v0.1.0",
    version = "0.1.0"
    )

def get_db() :
    db = SessionLocal()
    
    try :
        yield db
        
    finally:
        db.close()


@app.post("/api/v1/cards/", response_model = schemas.BusinessCard)
def create_card (card : schemas.BusinessCardCreate, db : Session = Depends(get_db)) :
    
    try : 
        payload = card.model_dump(exclude_none = True)
        print("🛠️ DEBUG payload:", payload)  
        db_card = models.BusinessCard(**payload)
        
        db.add(db_card)
        db.commit()
        db.refresh(db_card)
        
        return db_card
    
    except Exception as e :
        
        traceback.print_exc()
        
        raise HTTPException(status_code=500, detail=f"{e.__class__.__name__}: {e}")


@app.get("/api/v1/business_cards/{card_id}", response_model = schemas.BusinessCard)
def read_business_card(card_id : int, db : Session = Depends(get_db)) :
    
    card = db.query(models.BusinessCard).filter(models.BusinessCard.id == card_id).first()
    
    if not card : raise HTTPException(status_code = 404, detail = "BusinessCard not found")
    
    return card
