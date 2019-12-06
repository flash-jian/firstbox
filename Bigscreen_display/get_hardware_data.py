import time

from paho.mqtt import client as mqtt

from setting import MQTTHOST
from setting import MQTTPORT



# 传入主题和获取数据的数据的公共类
class Hardware_obj:

    def __init__(self,theme):
        super(Hardware_obj, self).__init__()
        self.mqttClient = mqtt.Client()
        self.mqttClient.user_data_set(theme)
        self.info = []

    # 链接成功回调函数
    def on_connect(self,client,theme,flags,rc):

        client.subscribe(theme)
        # print("连接回调")

    # 消息接受回调函数
    def on_message(self,client,userdata,msg):
        # print("信息接收回调")
        data = msg.topic + "         " + str(msg.payload)
        self.info.append(data)
        return self.info

    # 获取硬件的数据，返回列表
    def hardware_msg(self):
        self.mqttClient
        self.mqttClient.connect(MQTTHOST, MQTTPORT, 60)
        self.mqttClient.loop_start()

        flag = True
        while flag:
            try:
                self.mqttClient.on_connect = self.on_connect
                self.mqttClient.on_message = self.on_message
            except Exception as e:
                print("订阅失败原因：",e)
            time.sleep(1)
            if len(self.info) >= 1:
                flag = False
            elif len(self.info) == 0:
                flag = False

        return self.info




# if __name__ == '__main__':
#
#     # obj1 = Hardware_obj('sensor/2_4/state')
#     obj1 = Hardware_obj('#')
#     res = obj1.hardware_msg()
#
#     print(res)





