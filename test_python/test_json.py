import json

import jsonpath

r={
  "errcode": 0,
  "errmsg": "ok",
  "taglist": [
    {
      "tagid": 2,
      "tagname": "修改后的标签名"
    },
    {
      "tagid": 3,
      "tagname": "test004"
    },
    {
      "tagid": 4,
      "tagname": "test005"
    },
    {
      "tagid": 5,
      "tagname": "test002"
    }
  ]
}

# 从jsno数据中取值，判断数据是否在json中
def test_json():
    res=jsonpath.jsonpath(r,'$..tagname')
    print(res)  # 返回一个数组
    print(len(res))
    assert 'test002' in res

def test_loads():
  # 把Json格式字符串解码转换成Python对象
  strList = '[1, 2, 3, 4]'
  strDict = '{"city": "北京", "name": "大猫"}'
  strTrue = 'true'
  strFalse ='false'
  strNull = 'null'

  print(json.loads(strList))
  print(json.loads(strDict))
  print(json.loads(strTrue))
  print(json.loads(strFalse))
  print(json.loads(strNull))
  print(json.loads('409'))
  print(json.loads('980.099'))
