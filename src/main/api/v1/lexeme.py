from flask import Blueprint, request

from src.main.common import generate_response
from src.main.models.services.LexemeService import lexeme_service

lexeme_bp = Blueprint('lexeme', __name__, url_prefix='/lexeme')


@lexeme_bp.route('/create', methods=['POST'])
def create_lexeme():
    data = request.get_json()
    lexeme = lexeme_service.create_lexeme(data)
    return generate_response(201, lexeme)


@lexeme_bp.route('/get_by_paper_id/<int:collection_id>', methods=['GET'])
def get_by_collection_id(collection_id):
    lexemes = lexeme_service.get_by_collection_id(collection_id)
    return generate_response(200, lexemes)


@lexeme_bp.route('/update/<int:id>', methods=['PUT'])
def update_lexeme(id):
    data = request.get_json()
    lexeme = lexeme_service.update_lexeme(id, data)
    return generate_response(200, lexeme)


@lexeme_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_lexeme(id):
    lexeme_service.delete_lexeme(id)
    return generate_response(204)
