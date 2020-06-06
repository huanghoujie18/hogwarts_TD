def test_decode():
# 编码：把码位转换成字节序列（通俗来说：把字符串转换成用于存储或传输的字节序列，python中是.encode()）
# 解码：把字节序列转换成码位（通俗来说：把字节序列转换成人类可读的文本字符串,python中是.decode()）
    s='caf\xc3\xa9'
    str=s.encode('utf8')
    str=str.decode('utf8')
    print(str)

