import sys
import os

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, project_root)

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.backend.extensions import db

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get paths for templates and static files
frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend')
template_folder = os.path.join(frontend_path, 'templates')
static_folder = os.path.join(frontend_path, 'static')

# Initialize Flask app with frontend paths
app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-for-golden-hand')

# PostgreSQL Database Configuration
# Password URL-encoded: Y9*jj%0#r@6655 → Y9%2Ajj%250%23r%406655
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sifiso_user:Yj27zzRaaG990@localhost:5433/golden_hand_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)
migrate = Migrate(app, db)

# Import all models so SQLAlchemy can configure relationships
with app.app_context():
    from src.backend.models import user, lesson, quiz, audio, community, ai

# Register blueprints
from src.backend.routes.main import main_bp
from src.backend.routes.lessons import lessons_bp
from src.backend.routes.quiz import quiz_bp
from src.backend.routes.audio import audio_bp
from src.backend.routes.community import community_bp
from src.backend.routes.ai import ai_bp

app.register_blueprint(main_bp)
app.register_blueprint(lessons_bp, url_prefix='/lessons')
app.register_blueprint(quiz_bp, url_prefix='/quiz')
app.register_blueprint(audio_bp, url_prefix='/audio')
app.register_blueprint(community_bp, url_prefix='/community')
app.register_blueprint(ai_bp, url_prefix='/ai')

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
