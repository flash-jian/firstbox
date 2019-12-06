import pymysql

host = '192.168.188.208'
port = 3306
user = 'root'
password = 'root'
db = 'management_system'
charset = 'utf8'
cursorclass = pymysql.cursors.DictCursor

# 获取所有的硬件的场景
def all_hardwares_scenes():
    hardwares_scenes_dic = {}
    connection = pymysql.connect(host=host,
                                 port=port,
                                 user=user,
                                 password=password,
                                 db=db,
                                 charset=charset)

    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT component.entry_id,terminal.name FROM " \
                  "terminal_component LEFT JOIN component on " \
                  "terminal_component.component_id = component.entry_id " \
                  "left join terminal on terminal_component.terminal_id = terminal.id"

            cursor.execute(sql)
            result = cursor.fetchall()

    except Exception as e:
        print("management_system数据库获取属性失败原因:", e)
    finally:
        connection.close()

    for hardware in result:
        if hardware["entry_id"] not in hardwares_scenes_dic.keys():
            hardwares_scenes_dic[hardware["entry_id"]] = {"name":[hardware["name"]]}
        else:
            hardwares_scenes_dic[hardware["entry_id"]]["name"].append(hardware["name"])

    # print(hardwares_scenes_dic)
    return hardwares_scenes_dic

# if __name__ == '__main__':
#     all_hardwares_scenes()