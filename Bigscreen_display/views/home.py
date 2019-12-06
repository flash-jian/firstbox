from flask import Blueprint
from flask import render_template
index = Blueprint('home',__name__,template_folder="templates",static_url_path="\static")


@index.route('/index')
def home_page():
    return render_template("index.html")