# Import all models to ensure SQLAlchemy can configure relationships properly
from src.backend.models.user import User, QuizResult, LessonProgress, Project
from src.backend.models.lesson import Subject, Lesson, LessonResource
from src.backend.models.quiz import Quiz, Question, QuestionOption
from src.backend.models.audio import AudioLesson, AudioPlayback
from src.backend.models.community import Community, CommunityMembership, CommunityPost, PostComment, Startup, StartupTeam
from src.backend.models.ai import AIProject, AIDataset, AIModel, AITutorial

__all__ = [
    'User', 'QuizResult', 'LessonProgress', 'Project',
    'Subject', 'Lesson', 'LessonResource',
    'Quiz', 'Question', 'QuestionOption',
    'AudioLesson', 'AudioPlayback',
    'Community', 'CommunityMembership', 'CommunityPost', 'PostComment', 'Startup', 'StartupTeam',
    'AIProject', 'AIDataset', 'AIModel', 'AITutorial'
]
