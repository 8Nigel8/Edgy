from flask import Blueprint, request

from src.main.common import generate_response
from src.main.models.services.PaperService import paper_service

paper_bp = Blueprint('paper', __name__, url_prefix='/paper')


@paper_bp.route('/create', methods=['POST'])
def create_paper():
    data = request.get_json()
    paper = paper_service.create_paper(data)
    return generate_response(201, paper)

@paper_bp.route('/get_by_collection_id/<int:collection_id>', methods=['GET'])
def get_by_collection_id(collection_id):
    papers = paper_service.get_by_collection_id(collection_id)
    return generate_response(200,papers)

@paper_bp.route('/update/<int:id>', methods=['PUT'])
def update_paper(id):
    data = request.get_json()
    paper = paper_service.update_paper(id, data)
    return generate_response(200, paper)

@paper_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_paper(id):
    paper_service.delete_paper(id)
    return generate_response(204)