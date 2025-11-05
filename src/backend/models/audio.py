from src.backend.extensions import db
from datetime import datetime

class AudioLesson(db.Model):
    __tablename__ = 'audio_lessons'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    grade_level = db.Column(db.Integer)
    duration_minutes = db.Column(db.Integer)
    file_path = db.Column(db.String(255))
    language = db.Column(db.String(50), default='English')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<AudioLesson {self.title}>'


class AudioPlayback(db.Model):
    __tablename__ = 'audio_playbacks'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    audio_lesson_id = db.Column(db.Integer, db.ForeignKey('audio_lessons.id'))
    progress_seconds = db.Column(db.Integer, default=0)
    completed = db.Column(db.Boolean, default=False)
    last_played = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<AudioPlayback {self.id}>'
