from loguru import logger

from .Models import DataBase
from .Models.User import User
from .Models.Admin import Admin
#from .Models.Moderator import Moderator
from .session import Session
import settings






class UserManager():
  @logger.catch
  def __init__(self):
    DataBase.Init(settings.DB_CONN_STR)
    self._session = DataBase.GetSession()

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
      self._session.commit()
    return wrapper

  def MidlewareWrapper(self, func):
    def wrapper(bot, message):
      self._session = DataBase.GetSession()
      
      user = self._addandorgetuser(
          message.from_user.id, 
          message.from_user.username, 
          message.from_user.first_name, 
          message.from_user.last_name
        )
      s = Session(user, self._session)
      message.session : Session = s
      func(
        bot,
        message, 
      )
      self._session.commit()
      #self._session.close()
    return wrapper


  @logger.catch
  def AddUser(self, Tg_id, UserName, FirstName, LastName):
    self._addandorgetuser(Tg_id, UserName, FirstName, LastName)

  @logger.catch
  def _addandorgetuser(self, TgId, UserName, FirstName, LastName):
    u = self._session.query(User).filter_by(TgId=TgId).first()
    newuser = False
    if u is None:
      u = User(TgId, UserName, FirstName, LastName)
      self._session.add(u)
      self._session.commit()
      u = self._session.query(User).filter_by(TgId=TgId).first()
      newuser = True
    logger.debug(f"User <{u}> requesed ({'Alredy exists' if not newuser else 'Has been created'})")
    #session.close()
    return u

  @logger.catch
  def PromoteAdmin(self, user):
    
    admin = Admin(user)
    if self._session.query(Admin).filter_by(UserId=user.Id).first() is None:
      self._session.add(admin)
      self._session.commit()
    #self._session.close()
  

  def __del__(self):
    self._session.close()


