def server_ip():
    # 配置文件，通过修改配置，在不同环境进行测试
    dev_ip='https://www.baidu.com/'
    sit_ip='https://cn.bing.com/'
    return sit_ip

def sql_conf():
    # 定义数据库的配置
    ip=''
    username=''
    password=''
    port=3306
    charset='utf-8'
    return ip,username,password,port,charset
