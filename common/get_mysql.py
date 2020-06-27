import pymysql
from config.conf import sql_conf  #导入参数配置定义的函数
def get_sql(sql):
    # 建立一个连接对象
    host,user,password,database,port,charset=sql_conf() #引用参数配置的值
    db=pymysql.connect(host=host,user=user,database=database,port=port,charset=charset)
    # 建立一个游标
    cursor=db.cursor()
    # 运行sql语句
    cursor.execute(sql)
    # 保存查询的结果
    data=cursor.fetchall()

    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    db.close()
    # 返回数据
    return data

def test_get_sql():
    print(get_sql("SELECT dept_no FROM departments WHERE dept_name ='Finance'"))
