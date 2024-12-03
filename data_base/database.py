import openpyxl
import openpyxl.reader
import openpyxl.reader.excel

from datetime import date


def open_exel():
    try:
        wb = openpyxl.reader.excel.load_workbook(filename= "BD.xlsx")
        wb.active = 0
    except:
        print("Файл не найден")
    
    return wb
    

def output_sheet(wb):
    dt_now = date.today()

    sheet = wb.active

    for row in range(1, sheet.max_row):
        date_sale = sheet[row][0].value
        name = sheet[row][1].value
        category = sheet[row][2].value
        quantity = sheet[row][3].value
        cost = sheet[row][4].value
        print(dt_now == date_sale, str(dt_now), str(date_sale)[:10])
        #print(date_sale)
        #print(f"{str(date_sale)[:11]} {name} {category} {quantity} {cost}")

wb = open_exel()
output_sheet(wb)