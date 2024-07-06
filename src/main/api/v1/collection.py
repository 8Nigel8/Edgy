from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.main.common import generate_response
from src.main.models.services.CollectionService import collection_service

collection_bp = Blueprint('collection_bp', __name__, url_prefix='/collection')


@collection_bp.route('/get_all', methods=['GET'])
def get_all_collections():
    collections = collection_service.get_all_collections()
    return generate_response(200, collections)


@collection_bp.route('/create', methods=['POST'])
@jwt_required()
def create_collection():
    user_id = get_jwt_identity()
    data = request.get_json()
    data['user_id'] = user_id
    new_collection = collection_service.create_collection(data)
    return generate_response(201, new_collection)


@collection_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_collection(id):
    collection_service.delete_collection(id)
    return generate_response(204)


@collection_bp.route('/update/<int:id>', methods=['PUT'])
def update_collection(id):
    data = request.get_json()
    new_collection = collection_service.update_collection(id, data)
    return generate_response(200, new_collection)
