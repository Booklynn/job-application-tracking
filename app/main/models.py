from app.extensions import db
from datetime import datetime, timezone

class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    job_function = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    date_applied = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    status = db.Column(db.String(50), nullable=False, default="Applied")
    notes = db.Column(db.Text, nullable=True)
    
    user = db.relationship('User', backref=db.backref('job_applications', lazy=True))
    
    def __repr__(self):
        return f'<JobApplication {self.position} at {self.company}>'
