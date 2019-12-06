import requests
import json
import urllib3
import base64
import hmac
from hashlib import sha256
from setting import HIKVISION_KEY,HIKVISION_SECRET,HIKVISION_IP

class Hikvision(object):
    def __init__(self):
        urllib3.disable_warnings()
        self.host = r"https://" + HIKVISION_IP + r'/artemis'
        self.app_key = HIKVISION_KEY
        self.app_secret = HIKVISION_SECRET

    """获取签名加密"""

    def getSignature(self, url):
        METHOD = 'POST'
        Accept = '*/*'
        Content_Type = 'application/json'
        x_ca_signature_headers = 'x-ca-key'
        customHeaders = x_ca_signature_headers + ":" + self.app_key
        httpHeaders = METHOD + "\n" + Accept + "\n" + Content_Type + "\n" + customHeaders + "\n" + url
        signature = base64.b64encode(hmac.new(self.app_secret.encode('utf-8'),
                                              httpHeaders.encode('utf-8'), digestmod=sha256).digest()).decode()
        return signature

    """获取海康数据"""

    def getInformation(self, url_path, data_json):
        signature = self.getSignature("/artemis" + url_path)
        url = self.host + url_path
        header = {
            'method': 'POST',
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'x-ca-key': self.app_key,
            'x-ca-signature-headers': 'x-ca-key',
            'x-ca-signature': signature
        }
        result = requests.post(url=url, data=json.dumps(data_json), headers=header, verify=False).text
        return result

    """获取组织列表"""

    def getList(self):
        path = "/api/resource/v1/org/orgList"
        data = {
            "pageNo": 1,
            "pageSize": 1000
        }
        re = self.getInformation(path, data)
        re = json.loads(re)
        return re

    """获取监控点列表"""

    def getCameraList(self):
        path = "/api/resource/v1/camera/advance/cameraList"
        data = {
            "pageNo": 1,
            "pageSize": 1000,
            "treeCode": "0"
        }
        re = self.getInformation(path, data)
        re = json.loads(re)
        return re

    """获取监控点在线状态"""

    def getCamerastate(self):
        path = "/api/nms/v1/online/camera/get"
        data = {
            "pageNo": 1,
            "pageSize": 1000,
        }
        re = self.getInformation(path, data)
        re = json.loads(re)
        return re

    """获取监控视频流链接"""

    def getCameraVideoStream(self,cameraIndexCode):
        path = "/api/video/v1/cameras/previewURLs"
        data = {
            "cameraIndexCode": cameraIndexCode,
            "streamType": 0,
            "protocol": "hls",
            "transmode": 1
        }
        re = self.getInformation(path, data)
        re = json.loads(re)
        return re

# if __name__ == '__main__':
#     hik = Hikvision()
#     """获取监控状态"""
#     data = hik.getCameraVideoStream()
#     url = data["data"]["url"]
#     print(url)