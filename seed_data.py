from app import create_app, db
from app.models.user import User

app = create_app()

with app.app_context():
    username = app.config.get("ADMIN_USERNAME")
    email = app.config.get("ADMIN_EMAIL")
    password = app.config.get("ADMIN_PASSWORD")

    if not username or not email or not password:
        print("Admin credentials not set in instance/config.py")
        exit(1)

    admin = User.query.filter_by(username=username).first()
    if admin:
        print("Admin user already exists.")
    else:
        admin = User(username=username, email=email, role="Admin")
        admin.set_password(password)
        db.session.add(admin)
        db.session.commit()
        print("Admin user created.")