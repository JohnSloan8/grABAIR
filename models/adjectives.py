from pydantic import BaseModel
from typing import Optional


class POSDefaultAdjective(BaseModel):
    declension: Optional[str] = None
    disambig: Optional[str] = None
    sgNom: Optional[str] = None
    sgGenMasc: Optional[str] = None
    sgGenFem: Optional[str] = None
    plNom: Optional[str] = None
    graded: Optional[str] = None


class POSAdjective(BaseModel):
    default: POSDefaultAdjective
    number: str = None
    case: str = None
    gender: str = None
    eclipsed: bool = False
