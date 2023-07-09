from pydantic import BaseModel
from typing import Optional


class POSDefaultNoun(BaseModel):
    word: str = None
    declension: Optional[str] = None
    disambig: Optional[str] = None
    isProper: Optional[str] = None
    isImmutable: Optional[str] = None
    isDefinite: Optional[str] = None
    allowArticledGenitive: Optional[str] = None


class POSNoun(BaseModel):
    word: str = None
    unmodified_word: str = None
    default: POSDefaultNoun
    number: Optional[str] = None
    case: Optional[str] = None
    gender: Optional[str] = None
    strength: Optional[str] = None
    eclipsed: bool = False
    lenition: bool = False
    prefixT: bool = False
    prefixH: bool = False
