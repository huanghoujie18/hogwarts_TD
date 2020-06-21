import xlrd
def get_excel_row(row):  #row为第几行
    excel=xlrd.open_workbook('../test_data/usermessage.xlsx')  #使用相对路径，不要使用绝对路径
    table=excel.sheets()[0]  #读取第一页数据
    return table.cell_value(row,1),table.cell_value(row,2)  #读取传入行的第二列和第三列数据

def get_row(): #获取文件的总的函数
    excel=xlrd.open_workbook('../test_data/usermessage.xlsx')  #使用相对路径，不要使用绝对路径
    table=excel.sheets()[0]  #读取第一页数据
    return table.nrows

def get_dict(row):
    excel=xlrd.open_workbook('../test_data/dictmessage.xlsx')  #使用相对路径，不要使用绝对路径
    table=excel.sheets()[0]  #读取第一页数据
    return table.cell_value(row,1)

