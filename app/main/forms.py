#from wtforms.validators import Required
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,IntegerField,FileField

class UpdateProfile(FlaskForm):
   # bio = TextAreaField('Tell us about yourself', validators = [Required])
    submit = SubmitField('Submit')
                        
                        
class RecipeForm(FlaskForm):

    #name = StringField('Recipe name',validators=[Required()])
    #serving = IntegerField('Number of serving', validators=[Required()])
    image = FileField('Image')
    ingredients = TextAreaField('Ingredients')
    description = TextAreaField('Cooking Procedure')
    #country = StringField('Country of origin', validators=[Required()])
    submit = SubmitField('Submit')