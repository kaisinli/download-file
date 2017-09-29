from app import db

class Download(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    client_ip = db.Column(db.String(255), unique=True)
    timestamp = db.Column(db.String(255), unique=True)
    delay_time = db.Column(db.Integer)

    def __init__(self, client_ip, timestamp, delay_time):
        self.client_ip = client_ip
        self.timestamp = timestamp
        self.delay_time = delay_time

    def __repr__(self):
        return '<Download %r>' % self.client_ip
