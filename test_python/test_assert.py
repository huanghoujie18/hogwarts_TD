# 断言json格式
def test_assert():

    a = {
        "errcode": 0,
        "errmsg": "deleted"
    }
    assert a["errmsg"]=="deleted"
