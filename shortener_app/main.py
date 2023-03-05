"""
This is the main file for running the fast API.

Author: Alex Wendland
"""

# Main class to run a fast API.
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello World!"