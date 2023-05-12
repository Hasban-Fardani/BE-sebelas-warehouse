from .create_db import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from flask_login import UserMixin

class UserModel(db.Model, UserMixin):
    __tablename__ = 'operators'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(255), unique=True)
    NIP = Column(Integer, unique=True)
    password = Column(String(255))
    create_at = Column(DateTime, default=datetime.now)
    last_update = Column(DateTime, onupdate=datetime.now)

    def __repr__(self) -> str:
        return f"<{self.name} {self.NIP}>"

    # requirement for flask_login.LoginManager 
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.id)

    def load_user(self):
        return UserModel.query.get(int(id))