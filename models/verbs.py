from pydantic import BaseModel
from typing import Optional


class POSDefaultVerb(BaseModel):
    word: str = None
    disambig: Optional[str] = None


class POSVerb(BaseModel):
    word: str = None
    unmodified_word: str = None
    default: POSDefaultVerb
    tense: Optional[str] = None
    dependency: Optional[str] = False
    person: Optional[str] = None
    eclipsed: Optional[bool] = False
    lenition: Optional[bool] = False


class POSVerbalAdjective(BaseModel):
    word: str = None
    default: POSDefaultVerb


class POSVerbalNoun(BaseModel):
    word: str = None
    default: POSDefaultVerb
