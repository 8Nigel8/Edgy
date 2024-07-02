from src.main.models.daos import collection_dao
from src.main.models.models import Collection
from src.main.models.schemas import collection_schema, collections_schema


class CollectionService:
    def create_collection(self, data):
        new_collection = collection_dao.persist(data, collection_schema)
        return new_collection

    def get_all_collections(self):
        collections = collection_dao.get_all(collections_schema)
        return collections

    def delete_collection(self, id):
        collection_dao.delete(Collection, id)

    def update_collection(self, id, data):
        updated_collection = collection_dao.update(id, data, collection_schema)
        return updated_collection


collection_service = CollectionService()
