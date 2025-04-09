
from typing import Optional
from pydantic import BaseModel


class UnrefinedData(BaseModel):
    date: str
    files: int
    owner: str
