from fastapi import APIRouter, Security
from src.routes.utils.api_key import get_api_key
from src.routes.utils.database import table


router = APIRouter()


@router.get("/get_database_history")
async def get_database_history(api_key: str = Security(get_api_key)):
  result = []
  data = table.find({},{"_id": 0}).sort("date",-1)
  for item in data:
    result.append(item)
  return result