from flask import Flask


from views import home
from views import login
from views import energy_monitoring
from views import milieu_monitoring
from views import scenes_monitoring
from views import security_monitoring
from views import device_control

import setting


app = Flask(__name__,static_folder=setting.STATIC_FOLDER,template_folder=setting.TEMPLATES_FOLDER)
# app = Flask(__name__,static_folder="static",template_folder="templates")

app.register_blueprint(home.index)
app.register_blueprint(login.loginer)
app.register_blueprint(energy_monitoring.energy)
app.register_blueprint(milieu_monitoring.milieu)
app.register_blueprint(scenes_monitoring.scenes)
app.register_blueprint(security_monitoring.security)
app.register_blueprint(device_control.device)

