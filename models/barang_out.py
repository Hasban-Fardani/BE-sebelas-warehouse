from .create_db import BaseModel
from .user_model import User
from datetime import datetime
from flask_login import UserMixin
import peewee as p

class Barang_Keluar(BaseModel, UserMixin):
    id          = p.CharField(primary_key=True)
    operator_id = p.ForeignKeyField(User)
    item_name   = p.CharField(max_length=50, unique=True)
    item_code   = p.CharField(max_length=8, null=False)
    room_id     = p.IntegerField(unique=True, null=False)
    type        = p.CharField(max_length=15, null=False)
    brand       = p.CharField(max_length=15, null=False)
    note        = p.CharField(max_length=15, null=False)
    jumlah_b    = p.IntegerField()
    jumlah_kb   = p.IntegerField()
    jumlah_rb   = p.IntegerField()
    create_at   = p.DateTimeField(default=datetime.now)

    def __repr__(self) -> str:
        return f"<id:{self.id} name:{self.item_name} added by {self.operator_id}>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'operator_id': self.operator_id.id,
            'item_name': self.item_name,
            'item_code': self.item_code,
            'room_id': self.room_id,
            'type': self.type,
            'brand': self.brand,
            'note': self.note,
            'jumlah_b': self.jumlah_b,
            'jumlah_kb': self.jumlah_kb,
            'jumlah_rb': self.jumlah_rb,
            'create_at': self.create_at.isoformat()
        }
    