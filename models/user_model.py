from .create_db import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from flask_login import UserMixin

class UserModel(db.Model, UserMixin):
    __tablename__ = 'operators'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    email = Column(String(50), unique=True)
    type = Column(String(8), nullable=False)
    NI = Column(Integer, unique=True, nullable=False)
    password = Column(String(15), nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    last_update = Column(DateTime, onupdate=datetime.now)

    def __repr__(self) -> str:
        match self.type:
            case "operator" | "guru":
                return f"<{self.name} NIP {self.NI}>"
            case "siswa":
                return f"<{self.name} NIS {self.NI}>"
        
    # requirement for flask_login.LoginManager 
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.id)

    # def load_user(self):
    #     return UserModel.query.get(int(id))