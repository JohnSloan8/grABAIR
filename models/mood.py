from pydantic import BaseModel
from typing import Optional


class POSDefaultMood(BaseModel):
    word: str = None
    disambig: Optional[str] = None


class POSMood(BaseModel):
    word: str = None
    unmodified_word: str = None
    default: POSDefaultMood
    mood: Optional[str] = None
    person: Optional[str] = None
