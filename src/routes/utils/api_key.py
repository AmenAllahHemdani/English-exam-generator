from fastapi import HTTPException, status, Security
from fastapi.security import APIKeyQuery
from config import settings

api_key_query = APIKeyQuery(name="api-key", auto_error=False)

def get_api_key(api_key_query: str = Security(api_key_query)):

    if api_key_query == settings.API_KEY:
        return api_key_query
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )