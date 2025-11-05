"""
Seed script to populate the database with sample data
"""
from src.backend.main import app
from src.backend.extensions import db
from src.backend.models.lesson import Subject, Lesson

def seed_subjects():
    """Add sample subjects to the database"""

    subjects_data = [
        {
            'name': 'Mathematics',
            'description': 'Master mathematical concepts from basic arithmetic to advanced calculus and statistics.',
            'grade_level': 10
        },
        {
            'name': 'Science',
            'description': 'Explore the wonders of physics, chemistry, and biology through interactive lessons.',
            'grade_level': 10
        },
        {
            'name': 'English',
            'description': 'Develop reading, writing, and communication skills with comprehensive language lessons.',
            'grade_level': 10
        },
        {
            'name': 'History',
            'description': 'Journey through time and learn about African and world history, cultures, and civilizations.',
            'grade_level': 10
        },
        {
            'name': 'Programming',
            'description': 'Learn to code with Python, JavaScript, and other programming languages. Build real projects.',
            'grade_level': 10
        },
        {
            'name': 'Business Studies',
            'description': 'Understand entrepreneurship, marketing, finance, and how to start your own business.',
            'grade_level': 11
        },
        {
            'name': 'Computer Science',
            'description': 'Dive into algorithms, data structures, and computational thinking.',
            'grade_level': 12
        },
        {
            'name': 'Life Sciences',
            'description': 'Study living organisms, ecosystems, genetics, and the natural world.',
            'grade_level': 11
        },
        {
            'name': 'Physical Sciences',
            'description': 'Explore physics and chemistry concepts with practical applications.',
            'grade_level': 11
        },
        {
            'name': 'Economics',
            'description': 'Learn about markets, trade, financial systems, and economic principles.',
            'grade_level': 12
        },
        {
            'name': 'Geography',
            'description': 'Study maps, landforms, climate patterns, and human-environment interactions.',
            'grade_level': 10
        },
        {
            'name': 'Art & Design',
            'description': 'Express your creativity through visual arts, digital design, and creative projects.',
            'grade_level': 9
        }
    ]

    print(">> Seeding subjects...")

    for subject_data in subjects_data:
        # Check if subject already exists
        existing_subject = Subject.query.filter_by(name=subject_data['name']).first()
        if existing_subject:
            print(f"   [SKIP] {subject_data['name']} already exists")
            continue

        subject = Subject(**subject_data)
        db.session.add(subject)
        print(f"   [OK] Added: {subject_data['name']}")

    db.session.commit()
    print(">> Subjects seeded successfully!")

def seed_sample_lessons():
    """Add sample lessons for some subjects"""

    # Get Mathematics subject
    math_subject = Subject.query.filter_by(name='Mathematics').first()
    if math_subject:
        lessons_data = [
            {
                'title': 'Introduction to Algebra',
                'content': 'Learn the fundamentals of algebraic expressions and equations.',
                'subject_id': math_subject.id,
                'grade_level': 10,
                'difficulty': 'beginner',
                'duration_minutes': 45
            },
            {
                'title': 'Linear Equations',
                'content': 'Solve and graph linear equations in one and two variables.',
                'subject_id': math_subject.id,
                'grade_level': 10,
                'difficulty': 'intermediate',
                'duration_minutes': 60
            },
            {
                'title': 'Quadratic Functions',
                'content': 'Master quadratic equations, graphing parabolas, and finding roots.',
                'subject_id': math_subject.id,
                'grade_level': 10,
                'difficulty': 'advanced',
                'duration_minutes': 75
            }
        ]

        print("\n>> Seeding sample lessons...")
        for lesson_data in lessons_data:
            existing_lesson = Lesson.query.filter_by(title=lesson_data['title']).first()
            if existing_lesson:
                print(f"   [SKIP] {lesson_data['title']} already exists")
                continue

            lesson = Lesson(**lesson_data)
            db.session.add(lesson)
            print(f"   [OK] Added: {lesson_data['title']}")

        db.session.commit()
        print(">> Sample lessons seeded successfully!")

def main():
    """Main seeding function"""
    with app.app_context():
        print("\n" + "="*60)
        print("THE GOLDEN HAND - Database Seeding")
        print("="*60 + "\n")

        seed_subjects()
        seed_sample_lessons()

        # Print summary
        subject_count = Subject.query.count()
        lesson_count = Lesson.query.count()

        print("\n" + "="*60)
        print("Database Summary:")
        print("="*60)
        print(f"   Total Subjects: {subject_count}")
        print(f"   Total Lessons: {lesson_count}")
        print("="*60 + "\n")

if __name__ == '__main__':
    main()