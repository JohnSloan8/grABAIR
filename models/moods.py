from pydantic import BaseModel
from typing import Optional


class POSDefaultMood(BaseModel):
    word: str = None
    disambig: Optional[str] = None


class POSMood(BaseModel):
    POS: Optional[str] = None
    word: str = None
    mood: Optional[str] = None
    person: Optional[str] = None
    default: POSDefaultMood