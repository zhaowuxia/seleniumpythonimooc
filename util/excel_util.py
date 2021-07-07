
import xlrd
from xlutils.copy import copy
class excelutil:
    def __init__(self,excel_path=None,index=None):
        if excel_path==None:
            self.excel_path="D:\\python\\config\\casedata.xls"
        else:
            self.excel_path = excel_path
        if index==  None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)#整个excel的数据
        self.table = self.data.sheets()[index]

    #获取excel数据，按照每行一个list，添加到一个大的list中
    def get_data(self):
        result=[]
        rows = self.get_lines()
        if rows !=None:
            for i in range(rows):
                cal= self.table.row_values(i)#获取每一行的值
                result.append(cal)
            return result
        return None
    #获取excel的行数
    def get_lines(self):
        rows = self.table.nrows  # 获取行数
        if rows>=1:#为了保证获取的excel表格不为空
            return rows
        return None
    #获取单元格的数据,根据行号和列号
    def get_cal_value(self,row,cell):
        rows = self.get_lines()
        if rows>row:
            data = self.table.cell(row,cell).value
            return data
        return None
    #写入数据
    def write_value(self,row,value):
        raed_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(raed_value)#复制一份新的数据
        write_data.get_sheet(0).write(row,9,value)#将数据写入到指定的sheet页和指定的行和列
        write_data.save(self.excel_path)#写入后保存

if __name__ == '__main__':
    ex = excelutil('D:\\python\\config\\keyword.xls')
    print(ex.get_cal_value(5,7))