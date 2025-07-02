from app import app, db
from app.models import User, Attempt

with app.app_context():
    db.create_all()
