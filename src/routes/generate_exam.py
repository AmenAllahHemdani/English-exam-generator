from fastapi import APIRouter, HTTPException, Security
from datetime import datetime

from src.routes.utils.api_key import get_api_key
from utils.comprehension.text import get_format_reading_and_questions
from utils.languages.language import get_format_languages
from utils.writting.writing import get_format_writing
from src.routes.utils.database import table



router = APIRouter()

@router.post("/generate_exam/")
async def generate_exam(chapter: str, api_key: str = Security(get_api_key)):
    try:
        format_text = get_format_reading_and_questions(chapter)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Problem with generation text and questions: {str(e)}')

    try:
        format_language = get_format_languages()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Problem with generation language : {str(e)}')

    try:    
        format_writing = get_format_writing(chapter)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Problem with generation writing : {str(e)}')

    format_exam = format_text + '\n\n\n' + format_language + '\n\n\n' + format_writing

    date = datetime.now().strftime("%x")

    table.insert_one({'chapter':chapter , 'date': date , 'content':format_exam})

    return {'chapter':chapter , 'date': date , 'content':format_exam}
