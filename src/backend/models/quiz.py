from src.backend.extensions import db
from datetime import datetime

class Quiz(db.Model):
    __tablename__ = 'quizzes'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    grade_level = db.Column(db.Integer)
    difficulty = db.Column(db.String(20))  # beginner, intermediate, advanced
    time_limit_minutes = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    questions = db.relationship('Question', backref='quiz', lazy='dynamic')
    results = db.relationship('QuizResult', backref='quiz', lazy='dynamic')
    
    def __repr__(self):
        return f'<Quiz {self.title}>'


class Question(db.Model):
    __tablename__ = 'questions'
    
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'))
    question_text = db.Column(db.Text)
    question_type = db.Column(db.String(20))  # multiple_choice, true_false, short_answer
    points = db.Column(db.Integer, default=1)
    
    # Relationships
    options = db.relationship('QuestionOption', backref='question', lazy='dynamic')
    
    def __repr__(self):
        return f'<Question {self.id}>'


class QuestionOption(db.Model):
    __tablename__ = 'question_options'
    
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    option_text = db.Column(db.Text)
    is_correct = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<QuestionOption {self.id}>'
