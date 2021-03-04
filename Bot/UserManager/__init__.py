from loguru import logger

from .Models import DataBase
from .Models.User import User
import settings
#from Models.Admin import Admin
#from Models.Moderator import Moderator






class UserManager():
  @logger.catch
  def __init__(self):
    DataBase.Init(settings.DB_CONN_STR)
    self._session = None

  def RequirePermissin(self, **kwargs):
    return self.Wraps

  def Wraps(self, func):
    def wrapper(message):
      self._session = DataBase.GetSession()
      func(
        message, 
        self._addandorgetuser(
          message.from_user.id, 
          message.from_user.username, 
          message.from_user.first_name, 
          message.from_user.last_name
        )
      )
      self._session.close()
    return wrapper

  @logger.catch
  def AddUser(self, Tg_id, UserName, FirstName, LastName):
    self._session = DataBase.GetSession()
    self._addandorgetuser(Tg_id, UserName, FirstName, LastName)
    self._session.close()

  @logger.catch
  def _addandorgetuser(self, Tg_id, UserName, FirstName, LastName):
    u = User(Tg_id, UserName, FirstName, LastName)
    newuser = False
    if self._session.query(User).filter_by(Tg_id=Tg_id).first() is None:
      self._session.add(u)
      self._session.commit()
      newuser = True
    logger.debug(f"User <{u}> was requesed ({'Alredy exists' if not newuser else 'Has been created'})")
    #session.close()
    return u
