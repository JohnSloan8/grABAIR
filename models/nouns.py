from pydantic import BaseModel
from typing import Optional


class POSDefaultNoun(BaseModel):
    declension: Optional[str] = None
    disambig: Optional[str] = None
    isProper: Optional[str] = None
    isImmutable: Optional[str] = None
    isDefinite: Optional[str] = None
    allowArticledGenitive: Optional[str] = None


class POSNoun(BaseModel):
    default: POSDefaultNoun
    number: str = None
    case: str = None
    gender: str = None
    strength: Optional[str] = None
    eclipsed: bool = False
    prefixT: bool = False
    prefixH: bool = False
