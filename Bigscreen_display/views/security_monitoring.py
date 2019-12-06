from flask import Blueprint
from flask import request,jsonify
from flask import render_template
from hikvision import Hikvision
security = Blueprint('security_monitoring',__name__,template_folder="templates")

@security.route('/security')
def sccurity_page():
    return render_template("security.html")

@security.route('/videostream')
def getVideoStream():
    cameraIndexCode = request.args["cameraIndexCode"]
    hik = Hikvision()
    result = hik.getCameraVideoStream(cameraIndexCode)
    url = result["data"]["url"]
    return jsonify({'videostream':url})

@security.route('/hik')
def camera_page():
    return render_template("demo_window_simple_preview.html")

# @security.route('/a')
# def ceshia():
#     return render_template("a.html")







