from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



Base = declarative_base()


class DataBase():
  _name = ""
  _engine = None
  _session = None

  @classmethod
  def Init(cls, db: str):
    cls._name = db

  @classmethod
  def GetSession(cls):
    cls._engine = create_engine(cls._name, connect_args={'check_same_thread': False})
    Base.metadata.create_all(bind=cls._engine)
    session = sessionmaker(bind=cls._engine)()
    cls._session = session
    return session



if __name__ == "__main__":
  # следующие строки будут выполнены если модуль будет не импортирован, а запущен
  # команда для дебагинга: python -i Bot\UserManager\User.py
  DataBase.Init("sqlite:///../../../Data/UsersDB.sqlite3")
  session = DataBase.GetSession()