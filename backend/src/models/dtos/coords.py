from pydantic import BaseModel

class Coords(BaseModel):
    start: str
    end: str
    data_structure: str