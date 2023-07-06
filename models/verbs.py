from pydantic import BaseModel
from typing import Optional


class POSDefaultVerb(BaseModel):
    disambig: Optional[str] = None


class POSVerb(BaseModel):
    default: POSDefaultVerb
    tense: str = None
    dependency: str = None
    person: str = None
    eclipsed: bool = False
    prefixT: bool = False
    prefixH: bool = False
