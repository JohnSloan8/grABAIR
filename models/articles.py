from pydantic import BaseModel

class POSArticle(BaseModel):
    word: str
    number: str
