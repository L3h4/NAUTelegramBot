from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class User(Base):
  __tablename__ = "Users"

  Id = Column(Integer, primary_key=True)
  TgId = Column(Integer, unique=True, nullable=False)
  UserName = Column(String)
  FirstName = Column(String)
  LastName = Column(String)
  Admin = relationship("Admin",  uselist=False, back_populates="User")


  def __init__(self, TgId, UserName, FirstName, LastName):
    self.TgId = TgId
    self.UserName = UserName
    self.FirstName = FirstName
    self.LastName = LastName

  @property
  def is_admin(self):
    return self.Admin != None
    

  def __repr__(self):
    return f"{self.TgId}@{'*none*' if self.UserName in [None, ''] else self.UserName} ({self.FirstName} {self.LastName})"
