import threading
import paho.mqtt.client as mqtt
import time
import ast

HOST = "192.168.188.207"
PORT = 1883


class Mqtt_subscribe(threading.Thread):
    """
    mqtt thread, 完成订阅功能
    """

    def __init__(self, subtopic):
        super(Mqtt_subscribe, self).__init__()
        # self.client_id = time.strftime(
        #     '%Y%m%d%H%M%S', time.localtime(
        #         time.time()))

        # self.client = mqtt.Client(self.client_id)
        self.client = mqtt.Client(clean_session=True)
        self.client.user_data_set(subtopic)
        # self.client.username_pw_set("admin", "public")
        # self.tid = None
        # self.macaddress = None
        # self.type = None
        # self.status = None
        # self.subtype = None
        # self.info = None
        # self.answer_result = None

    def run(self):
        # ClientId不能重复，所以使用当前时间
        # 必须设置，否则会返回「Connected with result code 4」
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        time.sleep(2)
        self.client.on_disconnect = self.on_disconnect
        self.client.connect(HOST, PORT, 60)
        self.client.loop_forever(timeout=10)

    def on_connect(self, client, subtopic, flags, rc):
        print("Connected with result code " + str(rc))
        print("topic:" + subtopic)
        client.subscribe(subtopic, 2)

    def on_message(self, client, userdata, msg):
        # print(msg.topic + " " + msg.payload.decode("utf-8"))
        mess = msg.payload.decode("utf-8")
        print("############",mess)
        #在此处处理订阅主题返回的信息
        user_dict = ast.literal_eval(mess)
        self.answer_result = user_dict
        self.tid = user_dict['tid']
        self.macaddress = user_dict['macaddr']
        try:
            self.type = user_dict['type']
        except BaseException:
            pass
        try:
            self.subtype = user_dict['subtype']
        except BaseException:
            pass
        try:
            self.info = user_dict['info']
        except BaseException:
            pass
        try:
            self.status = user_dict['status']
        except BaseException:
            pass
        if self.macaddress and self.tid:
            self.client.disconnect()


        # return self.macaddress, self.tid, self.status, self.type, self.info, self.subtype
        print(self.macaddress, self.tid, self.status, self.type, self.info, self.subtype)

    def on_disconnect(self,client, userdata,rc):
        print(rc)



# if __name__ == "__main__":
#     subtopic = "sensor/1_4/state"
#     t = Mqtt_subscribe(subtopic)
#     a = t.client
#     t.start()
