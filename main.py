from src.routes.text import generate_reading_and_questions
from src.routes.language import generate_languages
from src.routes.writing import generate_writing
from src.routes.database import insert, loading
from dotenv import dotenv_values
from fastapi import HTTPException, status, Security, FastAPI
from fastapi.security import APIKeyHeader, APIKeyQuery
from pymongo import MongoClient

from datetime import datetime

app = FastAPI()

config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

api_key_query = APIKeyQuery(name="api-key", auto_error=False)


API_KEY = config["API_KEY"]


def get_api_key(api_key_query: str = Security(api_key_query)):

    if api_key_query == API_KEY:
        return api_key_query
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )

@app.post("/exam")
async def exam(chapter,api_key: str = Security(get_api_key)):

    try:
        text = generate_reading_and_questions(chapter)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Problem with generation text : {str(e)}')

    try:
        language = generate_languages()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Problem with generation language : {str(e)}')

    try:    
        writing = generate_writing(chapter)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Problem with generation writing : {str(e)}')

    result = text + '\n\n\n' + language + '\n\n\n' + writing

    date = datetime.now().strftime("%x")

    insert({'chapter':chapter , 'date': date , 'content':result})

    return {'chapter':chapter , 'date': date , 'content':result}


@app.get("/load")
async def load(chapter,api_key: str = Security(get_api_key)):
    result = loading(chapter)
    return result