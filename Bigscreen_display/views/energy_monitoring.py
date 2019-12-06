
from flask import Blueprint
from flask import render_template
energy = Blueprint('energy_monitoring',__name__,template_folder="templates")


@energy.route('/energy')
def energy_page():
    return render_template("energy.html")










