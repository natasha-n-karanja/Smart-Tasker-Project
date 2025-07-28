from flask import Blueprint, request, jsonify
from app.services.gemini_ai import suggest_goals, interpret_task

gemini_bp = Blueprint('gemini', __name__, url_prefix='/gemini')

@gemini_bp.route('/suggest', methods=['POST'])
def suggest():
    data = request.get_json()
    return jsonify(suggestions=suggest_goals(data['tasks']))

@gemini_bp.route('/interpret', methods=['POST'])
def interpret():
    data = request.get_json()
    return jsonify(interpretation=interpret_task(data['description']))
