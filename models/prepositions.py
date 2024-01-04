from pydantic import BaseModel
from typing import Optional


class POSDefaultPreposition(BaseModel):
    word: str = None
    disambig: Optional[str] = None
    sg1: Optional[str] = None
    sg2: Optional[str] = None
    sg3Masc: Optional[str] = None
    sg3Fem: Optional[str] = None
    pl1: Optional[str] = None
    pl2: Optional[str] = None
    pl3: Optional[str] = None


class POSPreposition(BaseModel):
    POS: Optional[str] = None
    word: str = None
    person: Optional[str] = None
    case: Optional[str] = None
    gender: Optional[str] = None
    default: POSDefaultPreposition
