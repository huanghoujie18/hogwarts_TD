import requests
from common.get_mysql import get_sql
def test_get_mysql():
    url='http//:127.0.0.1:8080'
    id=get_sql("SELECT dept_no FROM departments WHERE dept_name ='Finance'")
    data={'name':'Finance','id':id}
    r=requests.post(url=url,data=data)
    print(r.status_code)
    print(r.text)
