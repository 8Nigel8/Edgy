from src.main.consts import MAX_NAME_LENGTH
from src.main.extention import db


class Collection(db.Model):
    __tablename__ = 'collection'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(MAX_NAME_LENGTH), unique=True)
    description = db.Column(db.String(1000))

    papers = db.relationship('Paper', back_populates='collection')

    def __repr__(self):
        return '<Collection %r>' % self.name


class Paper(db.Model):
    __tablename__ = 'paper'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(MAX_NAME_LENGTH), unique=True)
    description = db.Column(db.String(1000))
    context = db.Column(db.String(1000))
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'))

    collection = db.relationship('Collection', back_populates='papers')
    lexemes = db.relationship('Lexeme', back_populates='paper')

    def __repr__(self):
        return '<Paper %r>' % self


class Lexeme(db.Model):
    __tablename__ = 'lexeme'
    id = db.Column(db.Integer, primary_key=True)
    original_text = db.Column(db.String(1000))
    translated_text = db.Column(db.String(1000))
    context = db.Column(db.String(1000))
    paper_id = db.Column(db.Integer, db.ForeignKey('paper.id'))

    paper = db.relationship('Paper', back_populates='lexemes')

    def __repr__(self):
        return '<Lexeme %r>' % self
