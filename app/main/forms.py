from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,IntegerField,FileField
from wtforms.validators import Required

class RecipeForm(FlaskForm):

    name = StringField('Recipe name',validators=[Required()])
    serving = IntegerField('Number of serving', validators=[Required()])
    image = FileField('Image')
    ingredients = TextAreaField('Ingredients')
    description = TextAreaField('Cooking Procedure')
    country = StringField('Country of origin', validators=[Required()])
    submit = SubmitField('Submit')