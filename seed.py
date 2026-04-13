import random
from datetime import datetime, timedelta
import os

from app import create_app, db
from app.models import User, Student, AcademicRecord, Socioeconomic

EDUCATION_LEVELS = ['Primary', 'High School', 'Bachelors', 'Masters', 'PhD']
COURSES = ['Computer Science', 'Business Administration', 'Engineering', 'Mathematics', 'Biology']
NAMES_FIRST = ['Alex', 'Jordan', 'Taylor', 'Morgan', 'Casey', 'Sam', 'Riley', 'Jamie', 'Charlie', 'Avery']
NAMES_LAST = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']

def generate_seed_data():
    app = create_app()
    with app.app_context():
        db.create_all()
        
        # Avoid reseeding
        if User.query.first():
            print("Database already seeded!")
            return
            
        print("Seeding Users...")
        admin = User(username='admin', email='admin@edu.com', role='Admin')
        admin.set_password('password123')
        teacher = User(username='teacher1', email='teacher1@edu.com', role='Teacher')
        teacher.set_password('password123')
        counselor = User(username='counselor1', email='counselor1@edu.com', role='Counselor')
        counselor.set_password('password123')
        db.session.add_all([admin, teacher, counselor])
        db.session.commit()
        
        print("Seeding 50 Students...")
        sql_inserts = []
        for i in range(1, 51):
            name = f"{random.choice(NAMES_FIRST)} {random.choice(NAMES_LAST)}"
            age = random.randint(18, 26)
            course = random.choice(COURSES)
            enrollment_date = datetime.now() - timedelta(days=random.randint(100, 1000))
            
            # Formulate realistic risk scenarios
            # 30% are high chance of dropout
            is_dropout_risk = random.random() < 0.3
            if is_dropout_risk:
                gpa = round(random.uniform(1.0, 2.5), 2)
                attendance = round(random.uniform(40.0, 75.0), 1)
                credits_ratio = random.uniform(0.3, 0.7)
                scholarship = False
                debtor = random.random() < 0.7  # 70% chance debtor
                parent_ed = random.choice(['Primary', 'High School'])
                status = 'dropout' if random.random() < 0.5 else 'enrolled'
            else:
                gpa = round(random.uniform(2.5, 4.0), 2)
                attendance = round(random.uniform(75.0, 100.0), 1)
                credits_ratio = random.uniform(0.7, 1.0)
                scholarship = random.random() < 0.4 # 40% chance
                debtor = random.random() < 0.1 # 10% chance debtor
                parent_ed = random.choice(['Bachelors', 'Masters', 'PhD', 'High School'])
                status = 'graduated' if random.random() < 0.2 else 'enrolled'
                
            student = Student(
                name=name, age=age, gender=random.choice(['Male', 'Female', 'Non-binary']),
                course=course, enrollment_date=enrollment_date, status=status
            )
            db.session.add(student)
            db.session.commit() # commit to get student ID

            credits_attempted = random.randint(15, 60)
            credits_earned = int(credits_attempted * credits_ratio)
            
            ar = AcademicRecord(
                student_id=student.id, semester=random.randint(1, 4),
                gpa=gpa, credits_attempted=credits_attempted, credits_earned=credits_earned,
                attendance_pct=attendance, assignments_submitted=random.randint(5, 20)
            )
            
            se = Socioeconomic(
                student_id=student.id, scholarship_holder=scholarship,
                debtor=debtor, tuition_up_to_date=not debtor,
                parental_education_level=parent_ed, employment_status=random.choice(['Unemployed', 'Part-time', 'Full-time'])
            )
            db.session.add_all([ar, se])
            
            # Generate Raw SQL Insert string equivalent
            sql_inserts.append(f"INSERT INTO students (name, age, course, status) VALUES ('{name}', {age}, '{course}', '{status}');")
            
        db.session.commit()
        
        # Write sql file
        sql_path = os.path.join(os.path.dirname(__file__), 'migrations', '002_seed_data.sql')
        os.makedirs(os.path.dirname(sql_path), exist_ok=True)
        with open(sql_path, 'w') as f:
            f.write("\n".join(sql_inserts))
            
        print("Data generation complete and migrations/002_seed_data.sql created.")

if __name__ == '__main__':
    generate_seed_data()
