from src.main.extention import db
from src.main.models.daos import paper_dao
from src.main.models.models import Paper
from src.main.models.schemas import paper_schema


class PaperService:
    def create_paper(self, data):
        paper = paper_dao.persist(data, paper_schema)
        return paper

    def get_by_collection_id(self, collection_id):
        return paper_dao.get_by_collection_id(collection_id)

    def update_paper(self, id, data):
        updated_paper = paper_dao.update(id, data, paper_schema)
        return updated_paper

    def delete_paper(self, id):
        paper_dao.delete(Paper, id)


paper_service = PaperService()
