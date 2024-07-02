# todo
from src.main.extention import db


class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(1000))

    def __repr__(self):
        return '<Collection %r>' % self.name
