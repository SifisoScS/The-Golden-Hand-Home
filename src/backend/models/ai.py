from src.backend.extensions import db
from datetime import datetime

class AIProject(db.Model):
    __tablename__ = 'ai_projects'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    project_type = db.Column(db.String(50))  # chatbot, image_recognition, nlp, etc.
    status = db.Column(db.String(20))  # draft, in_progress, completed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    datasets = db.relationship('AIDataset', backref='project', lazy='dynamic')
    models = db.relationship('AIModel', backref='project', lazy='dynamic')
    
    def __repr__(self):
        return f'<AIProject {self.title}>'


class AIDataset(db.Model):
    __tablename__ = 'ai_datasets'
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ai_projects.id'))
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    file_path = db.Column(db.String(255))
    data_type = db.Column(db.String(50))  # text, image, audio, tabular
    size_mb = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<AIDataset {self.name}>'


class AIModel(db.Model):
    __tablename__ = 'ai_models'
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ai_projects.id'))
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    model_type = db.Column(db.String(50))  # classification, regression, generative
    architecture = db.Column(db.String(100))  # cnn, rnn, transformer, etc.
    accuracy = db.Column(db.Float)
    file_path = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<AIModel {self.name}>'


class AITutorial(db.Model):
    __tablename__ = 'ai_tutorials'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    content = db.Column(db.Text)
    difficulty = db.Column(db.String(20))  # beginner, intermediate, advanced
    category = db.Column(db.String(50))  # machine_learning, deep_learning, nlp, etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<AITutorial {self.title}>'
