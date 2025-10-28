from pydantic import BaseModel

class BinRes(BaseModel):
    binary_input: int
    base_10_output: int