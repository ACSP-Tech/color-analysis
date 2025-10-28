from sqlmodel import SQLModel, Field, Column, String, Integer
import uuid

class Color(SQLModel, table=True):
    """ Table define for question: Save the colours and their frequencies in postgresql database"""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), 
                    sa_column=Column(String(36), primary_key=True, nullable=False))
    color: str = Field(sa_column=Column(String(50), nullable=False, index=True))
    frequency: int = Field(sa_column=Column(Integer, nullable=False, index=True))