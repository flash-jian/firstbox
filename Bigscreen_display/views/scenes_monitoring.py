
from flask import Blueprint
from flask import render_template
scenes = Blueprint('scenes_monitoring',__name__,template_folder="templates")


@scenes.route('/scenes')
def scenes_page():
    return render_template("scenes.html")










