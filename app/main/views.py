from flask import render_template,request,redirect,url_for,flash,abort
from . import main
from ..models import Recipe, User
from .forms import RecipeForm, UpdateProfile
from .. import photos,db
import markdown2

# Views
@main.route('/')
def index():
  
  title = "Homepage"
  return render_template('index.html', title=title)


#Profile Route
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None: #if no user is found, then 'abort'
        abort(404)
    return render_template("profile/profile.html", user = user)

#UpdateProfile
@main.route('/user/<uname>/update', methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.username))
    
    return render_template('profile/update.html', form = form)

@main.route('/user/<uname>/update/pic', methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path #figure the name of this from whoever is doing models

        db.session.commit()

    return redirect(url_for('main.profile', uname  = uname))


@main.route('/recipies')
def all_recipes():
  recipes = Recipe.get_recipes()
  return render_template('recipe/all_recipes.html',recipes=recipes )

@main.route('/recipes/new',methods = ['GET', 'POST'])
def new_recipe():
  form = RecipeForm()
  if form.validate_on_submit():
    filename= photos.save(form.image.data)

    new_recipe = Recipe(name=form.name.data, num_of_servings =form.serving.data,
    image = filename,ingredients = form.ingredients.data, 
    description = form.description.data,country = form.country.data)

    new_recipe.save()

    flash('Your recipe has been created successfully')
    return redirect(url_for('main.all_recipes'))
  return render_template('recipe/new_recipe.html', title = "New Pitch", form = form)

@main.route('/recipes/<int:id>', methods=['GET'])
def view_recipe(id):
  recipe = Recipe.query.get(id)
  print(recipe)
  if recipe is None:
    abort(404)
  format_recipe = markdown2.markdown(recipe.ingredients, extras=["code-friendly", "fenced-code-blocks"])

  return render_template('recipe/recipe.html', format_recipe=format_recipe, recipe=recipe)

