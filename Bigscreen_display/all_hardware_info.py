from db_get_hardwares_attr import all_hardwares_attr
from db_get_hardwares_scenes import all_hardwares_scenes
from get_hardware_data import Hardware_obj
from setting import hardwares

# # 抽成一个公共类
class Public:
    hardwares_dic = {}
    def __init__(self,category):
        self.category = category

    # category时调用类的类别数组
    def get_data(self):
        hardwares_attr = all_hardwares_attr()
        hardwares_scenes = all_hardwares_scenes()
        for hardware in hardwares_attr.values():
            # 大字典中的小字典
            hardware_dic = {}
            if hardware['ctype'] == self.category[0] and hardware["cctype"] == self.category[1] \
                    and hardware["entry_id"] in hardwares_scenes.keys():
                # 拼接主题通过mqtt协议获取数据
                theme = hardware['ctype'] + '/' + hardware['entry_id'] + '/' + 'state'
                print("主题",theme)
                result = Hardware_obj(theme)
                hardware_data = result.hardware_msg()

                if not hardware_data:
                    continue
                hardware_data = result.hardware_msg()[0]
                hardware_data = hardware_data.split(" ")[-1]
                hardware_data = hardware_data.replace('\'','')[1:]

                # 将数据装入字典
                hardware_dic['entry_id'] = hardware['entry_id']
                hardware_dic['ctype'] = hardware['ctype']
                hardware_dic['cctype'] = hardware['cctype']
                hardware_dic['scenes'] = hardwares_scenes[hardware["entry_id"]]["name"]
                hardware_dic["data"] = hardware_data
            else:
                continue
            Public.hardwares_dic[hardware['entry_id']] = hardware_dic
            print(Public.hardwares_dic)
        return Public.hardwares_dic

# 湿度计获取数据功能类
class Humidity:

    def __init__(self):
        # super(Public,self).__init__()
        self.humiditys_dic = None

    def get_hardware_data(self):
        for key,category in hardwares.items():
            if key == "humidity":
                obj = Public(category)
                self.humiditys_dic = obj.get_data()
        return self.humiditys_dic

# 温度计获取数据功能类
class Temperature:
    def __init__(self):
        # super(Public,self).__init__()
        self.thermemothers_dic = None

    def get_hardware_data(self):
        for key,category in hardwares.items():
            if key == "temperature":
                obj = Public(category)
                self.thermemothers_dic = obj.get_data()
        return self.thermemothers_dic

# 烟雾报警器获取数据功能类
class Smog:
    def __init__(self):
        # super(Public,self).__init__()
        self.somg_detectors_dic = None

    def get_hardware_data(self):
        for key,category in hardwares.items():
            if key == "smog":
                obj = Public(category)
                self.somg_detectors_dic = obj.get_data()

        return self.somg_detectors_dic

# 分贝仪获取数据功能类
class Noise:
    def __init__(self):
        # super(Public,self).__init__()
        self.decibel_meters_dic = None

    def get_hardware_data(self):
        for key,category in hardwares.items():
            if key == "noise":
                obj = Public(category)
                self.decibel_meters_dic = obj.get_data()
        return self.decibel_meters_dic

# 空调获取数据功能类
class Air_condition:
    pass







if __name__ == '__main__':
    # obj = Humidity()
    # obj.get_hardware_data()

    # obj = Temperature()
    # obj.get_hardware_data()

    # obj = Smog()
    # obj.get_hardware_data()

    obj = Noise()
    obj.get_hardware_data()



















