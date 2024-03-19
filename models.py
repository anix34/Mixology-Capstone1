# import json
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Drink(db.Model):
    __tablename__ = "drinks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text, nullable=True)
    instructions = db.Column(db.Text)
    ingredient1 = db.Column(db.Text)
    ingredient2 = db.Column(db.Text)
    ingredient3 = db.Column(db.Text)
    ingredient4 = db.Column(db.Text)
    ingredient5 = db.Column(db.Text)
    ingredient6 = db.Column(db.Text)
    ingredient7 = db.Column(db.Text)
    ingredient8 = db.Column(db.Text)
    ingredient9 = db.Column(db.Text)
    ingredient10 = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="cascade"))
    user = db.relationship('User', backref="drinks")

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'instructions': self.instructions,
            'ingredient1' : self.ingredient1,
            'ingredient2' : self.ingredient2,
            'ingredient3' : self.ingredient3,
            'ingredient4' : self.ingredient4,
            'ingredient5' : self.ingredient5,
            'ingredient6' : self.ingredient6,
            'ingredient7' : self.ingredient7,
            'ingredient8' : self.ingredient8,
            'ingredient9' : self.ingredient9,
            'ingredient10' : self.ingredient10,

        }

    def __repr__(self):
        return f"<drink name={self.name} category={self.category}             instructions = {self.instructions} ingredient1 = {self.ingredient1}ingredient2 = {self.ingredient2} ingredient3 = {self.ingredient3}ingredient4 = {self.ingredient4} ingredient5 = {self.ingredient5}ingredient6 = {self.ingredient6} ingredient7 = {self.ingredient7}ingredient8 = {self.ingredient8} ingredient9 = {self.ingredient9}ingredient10 = {self.ingredient10} ingredient11 = {self.ingredient11}ingredient12 = {self.ingredient12} ingredient13 = {self.ingredient13}ingredient14 = {self.ingredient14}ingredient15 = {self.ingredient15}>"

class AddDrink(db.Model):
  
    __tablename__ = 'add_drinks'
    
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True
    )

    drink_id = db.Column(
        db.Integer
        
    )

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(80), nullable=False)


    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}>"


    @classmethod
    def register(cls, username, pwd, email):
        """Register user w/hashed password & return user."""

        hashed_pwd = bcrypt.generate_password_hash(pwd).decode('UTF-8')

        # return instance of user w/username and hashed pwd
        return cls(username=username, password=hashed_pwd, email=email)

    @classmethod
    def authenticate(cls, username, pwd):
        """Validate that user exists & password is correct.

        Return user if valid; else return False.
        """

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(users.password, pwd):
            # return user instance
            return u
        else:
            return False
