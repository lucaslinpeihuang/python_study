# -*-coding:UTF-8 -*-
from xlrd import open_workbook

bk = open_workbook(r'D:\doc\emp.xls') #bk是Book类的对象
sheet = bk.sheet_by_name('empinfo') #sheet 是Sheet类的对象
# print(sheet.nrows) #调Sheet类的静态属性 nrows


#读有多少列
# print(sheet.nrows)
# 
# #读某单元格（ANALYST）
# cell_value = sheet.cell_value(12,6)
# print(sheet.cell_value)
# 
# #读整个第X（7）行数据
# print(sheet.row_values(11,4))
# 
# #读姓名这一列
# print(sheet.col_values(5,5,14))

#读整个列表数据 
row_values =sheet.row_values(5,4)
print(row_values)

for i in range():
    print(row_values)

# for i in range():






