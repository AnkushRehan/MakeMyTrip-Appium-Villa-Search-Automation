'''it will fetch the data from excel file and you can use this in any program'''
import openpyxl
def getData(path,sheet_name):
    workbook=openpyxl.load_workbook(path)
    sheet=workbook[sheet_name]
    max_rows=sheet.max_row
    max_cols=sheet.max_column
    alldata=[]#store all data from excel sheet
    for rows in range(2,max_rows+1):
        for cols in range(1,max_cols+1):
            data=sheet.cell(row=rows,column=cols).value
            alldata.append(data)
    return alldata# return the all data from excel  so that we can use in the test case
