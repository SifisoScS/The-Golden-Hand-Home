from flask import Blueprint, render_template, redirect, url_for, flash, request
from src.backend.models.lesson import Lesson, Subject

lessons_bp = Blueprint('lessons', __name__)

@lessons_bp.route('/')
def index():
    """Lessons platform home page"""
    subjects = Subject.query.all()
    return render_template('lessons/index.html', subjects=subjects)

@lessons_bp.route('/subject/<int:subject_id>')
def subject(subject_id):
    """Subject page with list of lessons"""
    subject = Subject.query.get_or_404(subject_id)
    lessons = Lesson.query.filter_by(subject_id=subject_id).all()
    return render_template('lessons/subject.html', subject=subject, lessons=lessons)

@lessons_bp.route('/lesson/<int:lesson_id>')
def lesson(lesson_id):
    """Individual lesson page"""
    lesson = Lesson.query.get_or_404(lesson_id)
    return render_template('lessons/lesson.html', lesson=lesson)

@lessons_bp.route('/grades')
def grades():
    """View lessons by grade level"""
    grade = request.args.get('grade', type=int)
    if grade:
        subjects = Subject.query.filter_by(grade_level=grade).all()
    else:
        subjects = []
    return render_template('lessons/grades.html', subjects=subjects, selected_grade=grade)
