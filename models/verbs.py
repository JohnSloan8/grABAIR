from pydantic import BaseModel
from typing import Optional


class POSDefaultVerb(BaseModel):
    word: str = None
    disambig: Optional[str] = None


class POSVerb(BaseModel):
    POS: Optional[str] = None
    word: str = None
    unmodified_word: str = None
    tense: Optional[str] = None
    dependency: Optional[str] = False
    person: Optional[str] = None
    eclipsed: Optional[bool] = False
    lenition: Optional[bool] = False
    default: POSDefaultVerb



class POSVerbalAdjective(BaseModel):
    POS: Optional[str] = None
    word: str = None
    default: POSDefaultVerb


class POSVerbalNoun(BaseModel):
    POS: Optional[str] = None
    word: str = None
    default: POSDefaultVerb
