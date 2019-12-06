import os

BASE_DIR = os.path.dirname(__file__)
# 模板目录
TEMPLATES_FOLDER = os.path.join(BASE_DIR, "templates")
# 静态文件目录
STATIC_FOLDER = os.path.join(BASE_DIR, "static")


# 链接mqtt的服务器的IP和端口
MQTTHOST = "192.168.188.207"
MQTTPORT = 1883


# 每个硬件对应的类别，key为子类，value为大类
hardwares = {
    "humidity":["sensor","humidity"],
    "temperature":["sensor","temperature"],
    "smog":["sensor","smog"],
    "noise":["sensor","noise"],
    "fresh_wind":"fresh_wind",
    "Air_condition":["climate","modbus_485"],
    "power":"socket",
    "light":"light",
    "wifi":"wifi",
    "wired_network":"wired_network",
    "water_detection":"",
    "face_spot":"face_spot",
    "car_spot":"car_spot",
    "elevator":"elevator",
    "projector":"projector",
    "sound":"sound",
    "camera":"camera",
    "tv":"tv"
}

HIKVISION_IP = '192.168.188.216'
HIKVISION_KEY = '27018101'
HIKVISION_SECRET = 'LwJtf28X9EkJu7Qt0ug0'




