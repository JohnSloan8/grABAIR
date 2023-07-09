from pydantic import BaseModel
from typing import Optional


class POSDefaultPronoun(BaseModel):
    word: str = None
    nom: Optional[str] = None
    acc: Optional[str] = None


class POSPronoun(BaseModel):
    word: str = None
    default: POSDefaultPronoun
    number: Optional[str] = None
    gender: Optional[str] = None
    form: Optional[str] = None
