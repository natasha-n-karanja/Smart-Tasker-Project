from flask import Blueprint, request, jsonify
from app.models.habit import Habit
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

habit_bp = Blueprint('habit', __name__, url_prefix='/habits')

@habit_bp.route('/', methods=['POST'])
@jwt_required()
def create_habit():
    user_id = get_jwt_identity()
    data = request.get_json()
    habit = Habit(name=data['name'], frequency=data['frequency'], user_id=user_id)
    db.session.add(habit)
    db.session.commit()
    return jsonify(message='Habit created')

@habit_bp.route('/', methods=['GET'])
@jwt_required()
def get_habits():
    user_id = get_jwt_identity()
    habits = Habit.query.filter_by(user_id=user_id).all()
    return jsonify([{'id': h.id, 'name': h.name, 'frequency': h.frequency} for h in habits])
