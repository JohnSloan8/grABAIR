from pydantic import BaseModel
from typing import Optional

class POSNoun(BaseModel):
    default: str 
    declension: Optional[str] = None
    disambig: Optional[str] = None
    isProper: Optional[str] = None
    isImmutable: Optional[str] = None
    isDefinite: Optional[str] = None
    allowArticledGenitive: Optional[str] = None
    word: str
    strength: Optional[str] = None
    gender: Optional[str] = None
    number: str
    case: Optional[str] = None
    eclipsed: bool = False
    prefixT: bool = False

class POSArticle(BaseModel):
    word: str
    number: str

class POSWord(BaseModel):
    word: str