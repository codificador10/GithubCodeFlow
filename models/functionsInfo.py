from pydantic import BaseModel
from typing import Optional

class functionInfo(BaseModel):
    fileName: str
    functionName: str
    functionBody: str
    functionClass: Optional[str] = None

    