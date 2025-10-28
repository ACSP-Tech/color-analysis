from pydantic import BaseModel
from typing import List

class SearchItem(BaseModel):
    target: int
    data_list: List[int]
    
class ReSear(BaseModel):
    target: int
    found: bool
    index: int = -1