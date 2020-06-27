def server_ip():
    # 配置文件，通过修改配置，在不同环境进行测试
    # dev_ip='https://www.baidu.com/'
    # sit_ip='https://cn.bing.com/'
    # 使用字典形式的参数化
    server_address={
    'dev_ip':'https://www.baidu.com/',
    'sit_ip':'https://cn.bing.com/'
    }
    # return sit_ip
    return server_address['dev_ip']  # 通过修改这里进行配置

def sql_conf():
    # 定义数据库的配置
    # host='127.0.0.1'
    # user='root'
    # password='123456'
    # database='employees'
    # port=3306
    # charset='utf8'
    # 列表参数化
    host,user,password,database,port,charset=['127.0.0.1','root','123456','employees',3306,'utf8']
    return host,user,password,database,port,charset
