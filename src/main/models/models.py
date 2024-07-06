from src.main.consts import MAX_NAME_LENGTH, MAX_EMAIL_LENGTH
from src.main.extention import db


class Collection(db.Model):
    __tablename__ = 'collection'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(MAX_NAME_LENGTH), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user'))

    papers = db.relationship('Paper', back_populates='collection')
    user = db.relationship('User', back_populates='collections')

    def __repr__(self):
        return '<Collection %r>' % self


class Paper(db.Model):
    __tablename__ = 'paper'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(MAX_NAME_LENGTH), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    context = db.Column(db.String(1000), nullable=False)
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'), nullable=False)

    collection = db.relationship('Collection', back_populates='papers')
    lexemes = db.relationship('Lexeme', back_populates='paper')

    def __repr__(self):
        return '<Paper %r>' % self


class Lexeme(db.Model):
    __tablename__ = 'lexeme'
    id = db.Column(db.Integer, primary_key=True)
    original_text = db.Column(db.String(1000), nullable=False)
    translated_text = db.Column(db.String(1000), nullable=False)
    context = db.Column(db.String(1000), nullable=False)
    paper_id = db.Column(db.Integer, db.ForeignKey('paper.id'), nullable=False)

    paper = db.relationship('Paper', back_populates='lexemes')

    def __repr__(self):
        return '<Lexeme %r>' % self


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(MAX_NAME_LENGTH), unique=True, nullable=False)
    # email = db.Column(db.String(MAX_EMAIL_LENGTH)) # TODO
    password_hash = db.Column(db.String(1000), nullable=False)

    collections = db.relationship('Collection', back_populates='user')

    def __repr__(self):
        return '<User %r>' % self
