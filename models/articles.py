from pydantic import BaseModel


class POSArticle(BaseModel):
    word: str = None
    number: str = None
