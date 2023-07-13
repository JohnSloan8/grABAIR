from pydantic import BaseModel


class POSDefaultArticle(BaseModel):
    word: str = None
    sg: str = None
    pl: str = None


class POSArticle(BaseModel):
    word: str = None
    default: POSDefaultArticle = None
    number: str = None
