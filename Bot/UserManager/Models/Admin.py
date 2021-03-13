from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .User import User
from . import Base

class Admin(Base):
  __tablename__ = "Admins"

  Id = Column(Integer, primary_key=True)
  UserId = Column(Integer, ForeignKey('Users.Id'), unique=True)
  User = relationship("User", back_populates="Admin")
  

  def __init__(self, User):
    self.User = User


  def __repr__(self):
    return f"{User} (Admin)"
