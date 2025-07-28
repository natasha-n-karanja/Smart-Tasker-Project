from flask import Blueprint, request, jsonify
from app.models.task import Task
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

task_bp = Blueprint('task', __name__, url_prefix='/tasks')

@task_bp.route('/', methods=['POST'])
@jwt_required()
def create_task():
    user_id = get_jwt_identity()
    data = request.get_json()
    task = Task(title=data['title'], description=data['description'], due_date=data['due_date'], user_id=user_id)
    db.session.add(task)
    db.session.commit()
    return jsonify(message="Task created"), 201

@task_bp.route('/', methods=['GET'])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': t.id,
        'title': t.title,
        'description': t.description,
        'due_date': t.due_date,
        'completed': t.completed
    } for t in tasks])

@task_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_task(id):
    task = Task.query.get(id)
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.due_date = data['due_date']
    task.completed = data['completed']
    db.session.commit()
    return jsonify(message="Task updated")

@task_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify(message="Task deleted")
