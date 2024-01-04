from pydantic import BaseModel
from typing import Optional

class POSParticle(BaseModel):
    POS: Optional[str] = None
    word: str
    type: str
