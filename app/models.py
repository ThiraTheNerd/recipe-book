from . import db
from datetime import datetime

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