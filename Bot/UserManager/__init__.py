from loguru import logger

from .Models import DataBase
from .Models.User import User
import settings
#from Models.Admin import Admin
#from Models.Moderator import Moderator



DataBase.Init(settings.DB_CONN_STR)

@logger.catch
class UserManager():
  def __init__(self):
    pass
  def AddUser(self, Tg_id, UserName, FirstName, LastName):
    session = DataBase.GetSession()
    u = User(Tg_id, UserName, FirstName, LastName)
    newuser = False
    if session.query(User).filter_by(Tg_id=Tg_id).first() is None:
      session.add(u)
      session.commit()
      newuser = True
    session.close()
    logger.debug(f"User <{u}> {'Alredy exists' if not newuser else 'Has been created'}")
    return newuser
  
  #def AddUserIfNeeded(self, Tg_id, UserName, FirstName, LastName):

