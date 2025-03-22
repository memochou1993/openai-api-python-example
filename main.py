import os

import requests
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import JSONResponse

load_dotenv(override=True)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/completions")
def create_completions():
    url = "https://api.openai.com/v1/completions"

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"}

    data = {"model": "gpt-3.5-turbo-instruct", "prompt": "Say this is a test", "max_tokens": 7, "temperature": 0}

    response = requests.post(url, json=data, headers=headers)

    return JSONResponse(content=response.json(), status_code=response.status_code)
