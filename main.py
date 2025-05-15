import logging
from fastapi import FastAPI, Request 
from fastapi.responses import JSONResponse

from src.routes import generate_exam, get_database_history


app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app.include_router(generate_exam.router)
app.include_router(get_database_history.router)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error"},
    )
