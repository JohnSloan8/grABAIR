from pydantic import BaseModel
from typing import Optional


class POSDefaultPronoun(BaseModel):
    word: str = None
    nom: Optional[str] = None
    acc: Optional[str] = None


class POSPronoun(BaseModel):
    POS: Optional[str] = None
    word: str = None
    number: Optional[str] = None
    gender: Optional[str] = None
    form: Optional[str] = None
    default: POSDefaultPronoun
