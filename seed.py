from app import app, db
from models import User

# Create tables
with app.app_context():
    db.create_all()

# Seed data
def seed_users():
    users = [
        {'username': 'user1', 'password': 'password1'},
        {'username': 'user2', 'password': 'password2'},
        # Add more users as needed
    ]

    for user_data in users:
        user = User(username=user_data['username'], password=user_data['password'])
        db.session.add(user)

    db.session.commit()

if __name__ == '__main__':
    seed_users()