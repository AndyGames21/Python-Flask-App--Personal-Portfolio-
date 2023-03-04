from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# Home View Route
@views.route('/home')
def home():
    return render_template("Python Website/home.html")

# About Me View Route
@views.route('/about')
def about():
    return render_template("Python Website/about_me.html")

# Projects View Route
@views.route('/projects')
def projects():
    return render_template("Python Website/projects.html")