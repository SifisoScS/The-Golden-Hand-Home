# The Golden Hand

## Overview

The Golden Hand is a comprehensive educational platform designed to empower South African students with digital technology skills and entrepreneurship mindset. The platform consists of five integrated components:

1. **Lessons Platform** - Structured, curriculum-aligned education for Grades 1-12 & Tertiary
2. **Quiz App** - Gamified, critical thinking-based mastery
3. **Audio Learning** - Accessible offline education by subject and grade
4. **Community Hub (SISONKE)** - Mentorship, peer support, and collaboration
5. **iKhaya AI** - A homegrown African AI hub for building AI solutions (Reserved for future development)

## Project Architecture

The project follows a clean separation between backend and frontend:

```bash
the-golden-hand/
├── src/
│   ├── backend/           # Python/Flask backend
│   │   ├── main.py       # Application entry point
│   │   ├── extensions.py # Flask extensions (SQLAlchemy)
│   │   ├── models/       # Database models
│   │   │   ├── user.py         # User, QuizResult, LessonProgress, Project
│   │   │   ├── lesson.py       # Subject, Lesson, LessonResource
│   │   │   ├── quiz.py         # Quiz, Question, QuestionOption
│   │   │   ├── audio.py        # AudioLesson, AudioPlayback
│   │   │   ├── community.py    # Community, Posts, Startups, Teams
│   │   │   └── ai.py           # AIProject, AIDataset, AIModel, AITutorial
│   │   └── routes/       # Route handlers (blueprints)
│   │       ├── main.py         # Landing, dashboard, profile
│   │       ├── lessons.py      # Lessons platform
│   │       ├── quiz.py         # Quiz app
│   │       ├── audio.py        # Audio learning
│   │       ├── community.py    # Community hub
│   │       └── ai.py           # iKhaya AI
│   │
│   └── frontend/          # Frontend assets
│       ├── templates/    # Jinja2 HTML templates
│       │   ├── index.html
│       │   ├── dashboard.html
│       │   ├── lessons/
│       │   ├── quiz/
│       │   ├── audio/
│       │   ├── community/
│       │   ├── ai/
│       │   └── errors/
│       └── static/       # CSS, JavaScript, images
│           ├── css/
│           ├── js/
│           └── images/
│
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create this)
└── README.md            # This file
```

## Technology Stack

### Backend

- **Flask 3.1.1** - Web framework
- **PostgreSQL** - Production database
- **SQLAlchemy 2.0.41** - ORM
- **Flask-Migrate 4.1.0** - Database migrations
- **psycopg2-binary 2.9.9** - PostgreSQL adapter

### Frontend

- **Jinja2 3.1.6** - Template engine
- **Tailwind CSS** - Styling framework
- **Vanilla JavaScript** - Interactive features

### Development

- **Flask-WTF 1.2.2** - Forms
- **python-dotenv 1.1.0** - Environment management

## Getting Started

### Prerequisites

- **Python 3.8+**
- **PostgreSQL 12+**
- **pip** (Python package manager)

### Database Setup

1. Install PostgreSQL and ensure it's running

2. The application is configured to connect to PostgreSQL with these credentials:
   - Host: `localhost`
   - Port: `5432`
   - Database: `golden_hand_db`
   - Username: `postgres`
   - Password: `Y9*jj%0#r@6655`

3. Create the database:

   ```sql
   CREATE DATABASE golden_hand_db;
   ```

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd the-golden-hand
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv

   # On Linux/Mac:
   source venv/bin/activate

   # On Windows:
   venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database:

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

### Running the Application

1. Start the Flask development server:

   ```bash
   python -m src.backend.main
   ```

2. Open your browser and navigate to:

   ```bash
   http://127.0.0.1:5000
   ```

## Features

### 1. Lessons Platform

- Structured, curriculum-aligned education
- Grade-specific content (Grades 1-12 & Tertiary)
- Subject categorization
- Interactive learning materials
- Progress tracking

### 2. Quiz App

- Gamified learning assessments
- Multiple choice, true/false, and short answer questions
- Critical thinking challenges
- Performance analytics
- Grade and difficulty level filtering

### 3. Audio Learning

- Offline-capable audio lessons
- Subject and grade categorization
- Playback progress tracking
- Perfect for students with limited internet access

### 4. Community Hub (SISONKE)

- Peer support and mentorship programs
- Startup team formation
- Community posts and discussions
- Events calendar
- Collaborative learning environment

### 5. iKhaya AI

- AI project development platform (Reserved for future)
- Tutorials and learning resources
- Dataset and model management
- AI playground for experimentation

## Key Changes from Previous Version

### Architecture Changes

- **Backend/Frontend Separation**: Clean separation of concerns with dedicated `backend/` and `frontend/` directories
- **Database Migration**: Changed from SQLite to PostgreSQL for production-ready scalability
- **Simplified Structure**: Removed AI agents system for streamlined development

### Authentication Changes

- **No Authentication Required**: All routes are now publicly accessible
- **Removed Flask-Login**: Simplified user management without authentication overhead
- **User Model Simplified**: Removed password hashing and authentication methods

### What Was Removed

- ❌ Specialized AI Agents system (Mathematics Navigator, Science Illuminator, Technology Architect)
- ❌ Flask-Login authentication middleware
- ❌ Password-based user authentication
- ❌ Login/registration routes and templates

### What Was Kept

- ✅ All 5 core applications (Lessons, Quiz, Audio, Community, iKhaya AI)
- ✅ Database models and relationships
- ✅ All existing features and functionality
- ✅ iKhaya AI app (reserved for future development)

## Database Models

### User Management

- `User` - User profiles with grade levels and roles
- `QuizResult` - Quiz performance tracking
- `LessonProgress` - Lesson completion tracking
- `Project` - User projects

### Learning Content

- `Subject` - Subject information
- `Lesson` - Lesson content and metadata
- `LessonResource` - Supplementary materials
- `Quiz`, `Question`, `QuestionOption` - Quiz system

### Audio Learning

- `AudioLesson` - Audio content
- `AudioPlayback` - Playback progress

### Community

- `Community` - Community groups
- `CommunityMembership` - User-community relationships
- `CommunityPost`, `PostComment` - Forum functionality
- `Startup`, `StartupTeam` - Startup collaboration

### AI Projects (Future)

- `AIProject` - AI project management
- `AIDataset` - Dataset storage
- `AIModel` - Model storage
- `AITutorial` - AI learning tutorials

## API Routes

### Main Routes

- `GET /` - Landing page
- `GET /dashboard` - User dashboard
- `GET /profile` - User profile

### Lessons Platform

- `GET /lessons/` - Lessons home
- `GET /lessons/subject/<id>` - Subject page
- `GET /lessons/lesson/<id>` - Lesson details
- `GET /lessons/grades` - Filter by grade

### Quiz App

- `GET /quiz/` - Quiz home
- `GET /quiz/<id>` - Quiz details
- `GET /quiz/<id>/start` - Start quiz
- `GET /quiz/<id>/results` - Quiz results

 Audio Learning

- `GET /audio/` - Audio home
- `GET /audio/<id>` - Audio details
- `GET /audio/<id>/play` - Play audio
- `GET /audio/by-subject` - Filter by subject
- `GET /audio/by-grade` - Filter by grade

### Community Hub

- `GET /community/` - Community home
- `GET /community/community/<id>` - Community details
- `GET /community/startups` - Startups listing
- `GET /community/startup/<id>` - Startup details
- `GET /community/mentorship` - Mentorship program
- `GET /community/events` - Community events

### iKhaya AI

- `GET /ai/` - iKhaya AI home
- `GET /ai/projects` - Projects listing
- `GET /ai/project/<id>` - Project details
- `GET /ai/tutorials` - Tutorials
- `GET /ai/playground` - AI playground
- `GET /ai/resources` - Learning resources

 Development

### Project Structure Conventions

- All backend Python code in `src/backend/`
- All frontend assets in `src/frontend/`
- Models use SQLAlchemy ORM
- Routes use Flask blueprints
- Templates use Jinja2 syntax

### Adding New Features

1. Create model in appropriate `models/` file
2. Create routes in appropriate `routes/` file
3. Create templates in `frontend/templates/`
4. Register blueprint in `main.py` if new

### Database Migrations

```bash
# Create migration
flask db migrate -m "Description of changes"

# Apply migration
flask db upgrade

# Rollback migration
flask db downgrade
```

## Vision

The Golden Hand is designed to help South African students learn digital technology and equip them to start their own businesses after Grade 12, rather than solely pursuing traditional higher education or employment. The platform nurtures entrepreneurial mindsets and practical skills for the digital economy.

## Accessibility Features

- High contrast mode
- Text size adjustment
- Multilingual support (planned)
- Offline capabilities for audio content
- Mobile-responsive design

## Future Roadmap

1. **Content Expansion**
   - Expand lesson library across all grade levels
   - Add more quizzes and assessments
   - Create more audio content

2. **Feature Development**
   - Implement full multilingual support (Zulu, Xhosa, Afrikaans)
   - Enhance offline capabilities
   - Build mobile applications (iOS/Android)
   - Develop iKhaya AI functionality

3. **Community Growth**
   - Build partnerships with schools
   - Engage with educational organizations
   - Create mentorship programs
   - Host virtual events

4. **Technical Improvements**
   - Performance optimization
   - Enhanced analytics and reporting
   - Real-time collaboration features
   - Progressive Web App (PWA) support

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

[Add your license information here]

## Support

For questions or support, please contact:

- Email: [Add contact email]
- Website: [Add website URL]

---

**The Golden Hand** - Empowering South African students with digital skills and entrepreneurship mindset.
