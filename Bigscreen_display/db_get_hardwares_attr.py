import pymysql

host = '192.168.188.208'
port = 3306
user = 'root'
password = 'root'
db = 'management_system'
charset = 'utf8'
cursorclass = pymysql.cursors.DictCursor

# 获取所有的硬件的属性
def all_hardwares_attr():
    hardwars_attr_dic = {}
    connection = pymysql.connect(host=host,
                                 port=port,
                                 user=user,
                                 password=password,
                                 db=db,
                                 charset=charset)

    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT %s,%s,%s,%s,%s FROM COMPONENT"\
                  % ('entry_id','friendly_name','ctype','cctype','comments')

            cursor.execute(sql)
            result = cursor.fetchall()
            # print(hardwars_attr_dic)
    except Exception as e:
        print("management_system数据库获取属性失败原因:",e)
    finally:
        connection.close()

    for hardwar in result:
        for key,value in hardwar.items():
            if key == "entry_id":
                hardwars_attr_dic[value] = hardwar
    # print(hardwars_attr_dic)
    return hardwars_attr_dic


# if __name__ == '__main__':
#     all_hardwares_attr()






