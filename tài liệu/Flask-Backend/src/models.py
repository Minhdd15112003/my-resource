from . import db
# from sqlalchemy.sql import func
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,TEXT
from sqlalchemy.orm import relationship

class Ddns(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    username = Column(String(100))
    password = Column(String(100))
    domain = Column(String(100))
    token = Column(String(100))
    status = Column(Boolean, default=False)
