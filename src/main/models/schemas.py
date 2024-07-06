from marshmallow import ValidationError, validates
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from src.main.consts import MIN_NAME_LENGTH, MAX_NAME_LENGTH
from src.main.extention import db
from src.main.models.models import Collection, Paper, Lexeme, User


class CollectionSchema(SQLAlchemySchema):
    class Meta:
        model = Collection
        load_instance = True
        sqla_session = db.session

    id = auto_field(dump_only=True)
    name = auto_field()
    description = auto_field()

    @validates('name')
    def validate_name(self, value):
        if not (MIN_NAME_LENGTH <= len(value) <= MAX_NAME_LENGTH):
            raise ValidationError("Name length must be between {} and {}".format(MIN_NAME_LENGTH, MAX_NAME_LENGTH))

    @validates('description')
    def validate_description(self, value):
        if len(value) > 1000:
            raise ValidationError("Max description length is {}".format(1000))


class PaperSchema(SQLAlchemySchema):
    class Meta:
        model = Paper
        load_instance = True
        sqla_session = db.session

    id = auto_field(dump_only=True)
    name = auto_field()
    description = auto_field()
    context = auto_field()
    collection_id = auto_field()

    @validates('name')
    def validate_name(self, value):
        if not (MIN_NAME_LENGTH <= len(value) <= MAX_NAME_LENGTH):
            raise ValidationError("Name length must be between {} and {}".format(MIN_NAME_LENGTH, MAX_NAME_LENGTH))

    @validates('description')
    def validate_description(self, value):
        if len(value) > 1000:
            raise ValidationError("Max description length is {}".format(1000))

    @validates('context')
    def validate_context(self, value):
        if len(value) > 1000:
            raise ValidationError("Max context length is {}".format(1000))


class LexemeSchema(SQLAlchemySchema):
    class Meta:
        model = Lexeme
        load_instance = True
        sqla_session = db.session

    id = auto_field(dump_only=True)
    translated_text = auto_field()
    original_text = auto_field()
    context = auto_field()
    paper_id = auto_field()

    @validates('translated_text')
    def validate_translated_text(self, value):
        if len(value) > 1000:
            raise ValidationError("Max text length is {}".format(1000))

    @validates('original_text')
    def validate_original_text(self, value):
        if len(value) > 1000:
            raise ValidationError("Max text length is {}".format(1000))

    @validates('context')
    def validate_context(self, value):
        if len(value) > 1000:
            raise ValidationError("Max context length is {}".format(1000))


class UserAuthenticationSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session

    id = auto_field(dump_only=True)
    username = auto_field()
    password_hash = auto_field()

    @validates('username')
    def validate_username(self, value):
        if not (MIN_NAME_LENGTH <= len(value) <= MAX_NAME_LENGTH):
            raise ValidationError("Username length must be between {} and {}".format(MIN_NAME_LENGTH, MAX_NAME_LENGTH))


class UserInfoSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session

    id = auto_field(dump_only=True)
    username = auto_field()


user_info_schema = UserInfoSchema()
user_authentication_schema = UserAuthenticationSchema()
lexeme_schema = LexemeSchema()
lexemes_schema = LexemeSchema(many=True)
paper_schema = PaperSchema()
papers_schema = PaperSchema(many=True)
collection_schema = CollectionSchema()
collections_schema = CollectionSchema(many=True)
