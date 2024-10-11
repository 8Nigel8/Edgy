from sqlalchemy import and_

from src.main.error_handlers import NotFoundException
from src.main.extention import db
from src.main.models.models import Paper, Lexeme, User, Collection
from src.main.models.schemas import papers_schema, lexemes_schema, user_authentication_schema, collections_schema


class BaseDao:
    @staticmethod
    def persist(data: dict, schema) -> dict:
        obj = schema.load(data)
        db.session.add(obj)
        db.session.commit()
        return schema.dump(obj)

    @staticmethod
    def update(id, data: dict, schema) -> dict:
        obj = db.session.query(schema.Meta.model).filter_by(id=id).first()

        if obj is None:
            raise NotFoundException("Object with id {} not found".format(id))
        updated_obj = schema.load(data, instance=obj)
        db.session.commit()
        return schema.dump(updated_obj)

    @staticmethod
    def delete(model, obj_id) -> None:
        db.session.query(model).filter(model.id == obj_id).delete()
        db.session.commit()

    @staticmethod
    def get_all(schema) -> list[dict]:
        objects = db.session.query(schema.Meta.model).all()
        return schema.dump(objects)

    @staticmethod
    def get_by_id() -> dict:
        ...


class CollectionDAO(BaseDao):
    def get_all(self, user_id) -> list[dict]:
        collections = db.session.query(Collection).filter(Collection.user_id == user_id).all()
        return collections_schema.dump(collections)

    def delete(self, collection_id, user_id) -> None:
        db.session.query(Collection) \
            .filter(
                and_(
                    (Collection.id == collection_id),
                    (Collection.user_id == user_id)
                )
            ).delete()
        db.session.commit()


class PaperDAO(BaseDao):
    def get_by_collection_id(self, collection_id: int) -> list[dict]:
        papers = db.session.query(Paper).filter(Paper.collection_id == collection_id).all()
        return papers_schema.dump(papers)


class LexemeDAO(BaseDao):
    def get_by_paper_id(self, paper_id: int) -> list[dict]:
        lexemes = db.session.query(Lexeme).filter(Lexeme.paper_id == paper_id).all()
        return lexemes_schema.dump(lexemes)


class UsersDAO(BaseDao):
    def get_by_username_for_login(self, username: str) -> list[dict]:
        user = db.session.query(User).filter(User.username == username).first()
        if user is None:
            raise NotFoundException("User not found")
        return user_authentication_schema.dump(user)


users_dao = UsersDAO()
lexeme_dao = LexemeDAO()
collection_dao = CollectionDAO()
paper_dao = PaperDAO()
