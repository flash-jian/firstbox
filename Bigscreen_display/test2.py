# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import json
import time

# 连接成功回调函数
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # 连接完成之后订阅gpio主题
    client.subscribe("#")
    # client.subscribe("sensor/2_4/state")

# 消息推送回调函数
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


if __name__ == '__main__':
    while 1:
        try:
            # a
            client = mqtt.Client()
            client.on_connect = on_connect
            client.on_message = on_message
            client.connect("192.168.188.207", 1883, 60)
            client.loop_forever()
        except:
            print("connect fail!")
            time.sleep(1)
