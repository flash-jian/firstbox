
from flask import Blueprint
from flask import render_template
device = Blueprint('device_control',__name__,template_folder="templates",)


@device.route('/device')
def device_page():
    return render_template("device.html")










