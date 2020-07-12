from os import listdir  # 从os模块导入listdir方法
def test_import2():
    # 列出指定目录的文件
    file=listdir('../config')
    print(file)
