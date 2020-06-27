import pytest

if __name__=="__main__":
    # 运行单个文件，添加对应文件的路径，使用相对路径
    # pytest.main(['../test_case/test_assert.py'])  # ../  run_case目录与test_requests属于同于层级，先回到上层目录，在进入test_requests
    # 运行多个文件，添加对应文件的路径，使用列表形式
    # pytest.main(['../test_case/test_assert.py','../test_case/test_assert1.py'])
    # 运行整个目录
    # pytest.main(['../test_case/'])
    # 生成hmtl报告，后面为路径和报告文件名称，'--html=../report/report.html'
    pytest.main(['../test_case/','--html=../report/report.html','--junitxml=../report/report.xml','--alluredir','../report/reportallure/'])


