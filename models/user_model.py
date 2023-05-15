from .create_db import BaseModel
from datetime import datetime
from flask_login import UserMixin
import peewee as p

class User(BaseModel, UserMixin):
    id          = p.IntegerField(primary_key=True)
    name        = p.CharField(max_length=30)
    email       = p.CharField(max_length=50, unique=True)
    type        = p.CharField(max_length=8, null=False)
    NI          = p.IntegerField(unique=True, null=False)
    password    = p.CharField(max_length=15, null=False)
    create_at   = p.DateTimeField(default=datetime.now)
    last_update = p.DateTimeField(default=datetime.now)

    def __repr__(self) -> str:
        match self.type:
            case "operator" | "guru":
                return f"<{self.name} NIP {self.NI}>"
            case "siswa":
                return f"<{self.name} NIS {self.NI}>"
    
    def __str__(self) -> str:
        return self.__repr__()
    # requirement for flask_login.LoginManager 
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.id)
    