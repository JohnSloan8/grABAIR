from pydantic import BaseModel
from typing import Optional

class POSDefaultArticle(BaseModel):
    word: str = None
    sg: str = None
    pl: str = None


class POSArticle(BaseModel):
    POS: Optional[str] = None
    word: str = None
    number: str = None
    default: POSDefaultArticle = None

