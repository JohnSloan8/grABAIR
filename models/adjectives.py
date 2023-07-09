from pydantic import BaseModel
from typing import Optional


class POSDefaultAdjective(BaseModel):
    word: str = None
    declension: Optional[str] = None
    disambig: Optional[str] = None
    sgNom: Optional[str] = None
    sgGenMasc: Optional[str] = None
    sgGenFem: Optional[str] = None
    plNom: Optional[str] = None
    graded: Optional[str] = None


class POSAdjective(BaseModel):
    word: str = None
    unmodified_word: str = None
    default: POSDefaultAdjective
    number: Optional[str] = None
    case: Optional[str] = None
    gender: Optional[str] = None
    graded: Optional[bool] = False
    lenition: Optional[bool] = False
