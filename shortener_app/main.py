"""
This is the main file for running the fast API.

Author: Alex Wendland
"""

# This is used to validated URLS
import validators

# Main class to run a fast API.
from fastapi import FastAPI, HTTPException

# This imports our schemas
from . import schemas

app = FastAPI()

# This will handle bad requests from the user.
def raise_bad_request(message: str):
    raise HTTPException(status_code=400, detail=message)

# This is the main route for the API, it doesn't do too much.
@app.get("/")
def read_root():
    return "Hello World!"

@app.post("/url")
def create_url(url: schemas.URLBase):
    if not validators.url(url.target_url):
        raise_bad_request("Invalid URL")
    return f"TODO: Create database entry for {url.target_url}"