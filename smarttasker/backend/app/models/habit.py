from app import db

class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    frequency = db.Column(db.String(20))  # daily/weekly
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
