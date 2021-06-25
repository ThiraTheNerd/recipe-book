from . import db
from datetime import datetime
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Recipe(db.Model):
  __tablename__ = 'recipes'
  id = db.Column(db.Integer, primary_key=True)
  name= db.Column(db.String(255))
  num_of_servings = db.Column(db.Integer, nullable=False)
  image=db.Column(db.String(255))
  ingredients = db.Column(db.String(255))
  description = db.Column(db.String(255))
  date_posted = db.Column(db.DateTime, default = datetime.utcnow(), nullable = False)
  country = db.Column(db.String(255))

  def save(self):
    db.session.add(self)
    db.session.commit()
  @classmethod
  def get_recipes(cls):
    all_recipies = Recipe.query.order_by(Recipe.date_posted.desc()).all()
    return all_recipies

  def __repr__(self):
    return f'User {self.name}'

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    email=db.Column(db.String(255), unique=True, index=True)
    username = db.Column(db.String(255))
    pass_secure=db.Column(db.String(255))
    password_hash=db.Column(db.String(255))
    bio=db.Column(db.String(255))
    profile_pic_path=db.Column(db.String())

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'
