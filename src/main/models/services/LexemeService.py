from src.main.extention import db
from src.main.models.daos import lexeme_dao
from src.main.models.models import Lexeme
from src.main.models.schemas import lexeme_schema


class LexemeService:
    def create_lexeme(self, data):
        lexeme = lexeme_dao.persist(data, lexeme_schema)
        return lexeme

    def get_by_collection_id(self, paper_id):
        return lexeme_dao.get_by_paper_id(paper_id)

    def update_lexeme(self, id, data):
        updated_lexeme = lexeme_dao.update(id, data, lexeme_schema)
        return updated_lexeme

    def delete_lexeme(self, id):
        lexeme_dao.delete(Lexeme, id)


lexeme_service = LexemeService()
