from flask import render_template,request,redirect,url_for
from . import main

# Views
@main.route('/')
def index():
  title = "Homepage"
  return render_template('index.html', title=title)