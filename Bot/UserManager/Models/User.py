from sqlalchemy import Column, Integer, String
from . import Base

class User(Base):
  __tablename__ = "Users"

  Id = Column(Integer, primary_key=True)
  Tg_id = Column(Integer, unique=True, nullable=False)
  UserName = Column(String)
  FirstName = Column(String)
  LastName = Column(String)

  def __init__(self, Tg_id, UserName, FirstName, LastName):
    self.Tg_id = Tg_id
    self.UserName = UserName
    self.FirstName = FirstName
    self.LastName = LastName

  def __repr__(self):
    return f"{self.Tg_id}@{'*none*' if self.UserName in [None, ''] else self.UserName} ({self.FirstName} {self.LastName})"
