from pydantic import BaseModel
from typing import Optional


class POSDefaultPossessive(BaseModel):
    word: str = None
    disambig: Optional[str] = None
    mutation: Optional[str] = None
    emphasizer: Optional[str] = None
    full: Optional[str] = None
    apos: Optional[str] = None


class POSPossessive(BaseModel):
    word: str = None
    default: POSDefaultPossessive
    number: Optional[str] = None
    gender: Optional[str] = None
    form: Optional[str] = None
