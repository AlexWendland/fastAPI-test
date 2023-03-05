"""
This is the main file for running the fast API.

Author: Alex Wendland
"""

# This is used to generate random strings
import secrets

# This is used to validated URLS
import validators

# Main class to run a fast API.
from fastapi import Depends, FastAPI, HTTPException

# Used for tpying
from sqlalchemy.orm import Session

# This imports our API schemas and database models
from . import models, schemas

# This imports connections to our database.
from .database import SessionLocal, engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# This will handle bad requests from the user.
def raise_bad_request(message: str):
    raise HTTPException(status_code=400, detail=message)

# This is the main route for the API, it doesn't do too much.
@app.get("/")
def read_root():
    return "Hello World!"

# This is the route to shorten a URL.
@app.post("/url", response_model=schemas.URLInfo)
def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):

    if not validators.url(url.target_url):
        raise_bad_request("Invalid URL")

    # Select characters to make the key and secret key from
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "".join(secrets.choice(chars) for _ in range(5))
    secret_key = "".join(secrets.choice(chars) for _ in range(8))

    # Add this URL to the database
    db_url = models.URL(key=key, secret_key=secret_key, target_url=url.target_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    # Update object to return to the user
    db_url.url = key
    db_url.admin_url = secret_key

    return db_url
