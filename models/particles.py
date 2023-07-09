from pydantic import BaseModel


class POSParticle(BaseModel):
    word: str
    type: str
