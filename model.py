from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

from db import Base

class testTable(Base):
    __tablename__ = 'test'
    # target table name inside the accessed db
    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String(58), nullable = False)
    age = Column(Integer, nullable = False)

class test(BaseModel):
    id: int
    name: str
    age: int