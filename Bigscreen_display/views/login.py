from flask import Blueprint
from flask import render_template
loginer = Blueprint('login',__name__)





@loginer.route('/')
def index():
    return render_template("login.html")