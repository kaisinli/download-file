from app import db
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.sql import func

class Download(db.Model):
    id = Column(Integer, primary_key = True)
    client_ip = Column(String(255))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    delay = Column(Integer)

    def __init__(self, client_ip, timestamp, delay):
        self.client_ip = client_ip
        self.delay = delay

    def __repr__(self):
        return '<Download %r>' % self.client_ip

