from pydantic import BaseModel


class POSWord(BaseModel):
    word: str = None
