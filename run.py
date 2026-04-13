from app import create_app, db
from app.models import User, Student, AcademicRecord, Socioeconomic, RiskScore, Intervention

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Student': Student, 'AcademicRecord': AcademicRecord,
            'Socioeconomic': Socioeconomic, 'RiskScore': RiskScore, 'Intervention': Intervention}

if __name__ == '__main__':
    app.run(debug=True, port=5000)
