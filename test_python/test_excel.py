import xlrd
def test_excel():
    excel=xlrd.open_workbook('../test_data/usermessage.xlsx')  #使用相对路径，不要使用绝对路径
    table=excel.sheets()[0]  # 读取第一页的信息，0表示第一页
    print(table.nrows)  #获取总的行数
    print(table.ncols)  #获取列的总数
    print(table.row_values(0))  #获取第一行的数据
    print(table.col_values(0))  #获取第一列的数据
    print(table.cell_value(0, 0))  #获取第一行第一列的数据，前面是行，后面是列
    for i in range(1,table.nrows):  #从第二行开始读取
        print(table.cell_value(i,1),table.cell_value(i,2))  #读取每一行的第二列和第三列
