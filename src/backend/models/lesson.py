from src.backend.extensions import db
from datetime import datetime

class Subject(db.Model):
    __tablename__ = 'subjects'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.Text)
    grade_level = db.Column(db.Integer)  # 1-12 for grades, 13+ for tertiary
    
    # Relationships
    lessons = db.relationship('Lesson', backref='subject', lazy='dynamic')
    
    def __repr__(self):
        return f'<Subject {self.name}>'


class Lesson(db.Model):
    __tablename__ = 'lessons'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    grade_level = db.Column(db.Integer)
    difficulty = db.Column(db.String(20))  # beginner, intermediate, advanced
    duration_minutes = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    progress = db.relationship('LessonProgress', backref='lesson', lazy='dynamic')
    resources = db.relationship('LessonResource', backref='lesson', lazy='dynamic')
    
    def __repr__(self):
        return f'<Lesson {self.title}>'


class LessonResource(db.Model):
    __tablename__ = 'lesson_resources'
    
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'))
    title = db.Column(db.String(100))
    resource_type = db.Column(db.String(50))  # video, document, link, code
    url = db.Column(db.String(255))
    content = db.Column(db.Text)  # For embedded content
    
    def __repr__(self):
        return f'<LessonResource {self.title}>'
