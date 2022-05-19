# import  openpyxl
# book = openpyxl.load_workbook(r'marks.xlsx')
# sheet = book["ClassA"]
#
# print(sheet["A10"].value)

import xlwings as xw
xw.books # Active app
wk  = xw.books.open(r'marks.xlsx')

sheet = wk.sheets("Results")
rg = sheet.range("A1:C2")

print(rg.value)

sheet.range("A16").value = "correct1"