


class Session():
  def __init__(self, user, db):
    self.user = user
    self.db = db
  
  def __del__(self):
    self.db.commit()