
from flask import Blueprint
from flask import render_template
milieu = Blueprint('milieu_monitoring',__name__,template_folder="templates")


@milieu.route('/milieu')
def milieu_page():
    return render_template("milieu.html")










