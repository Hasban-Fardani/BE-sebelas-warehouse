from .create_db import db
from sqlalchemy import Column, String, Integer

class BarangModel(db.Model):
    __tablename__ = "tbl_test_barang"
    id = Column(Integer, primary_key=True)
    nama = Column(String(50), nullable=False)
    jumlah = Column(Integer, nullable=False)
