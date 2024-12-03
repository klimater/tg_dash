import openpyxl
import openpyxl.reader
import openpyxl.reader.excel

from datetime import date

# Функция безопасного открытия файла
def open_exel(file_name):
    try:
        wb = openpyxl.reader.excel.load_workbook(filename= file_name)
        wb.active = 0
    except:
        print("Файл не найден")
        return None
    
    return wb
    
# Функция вывода даных из exel файла
def output_sheet(wb):
    if wb != None:
        sheet = wb.active
    else:
        return "Ошибка файл не найден"
    value = """"""
    for row in range(1, sheet.max_row):
        date_sale = sheet[row][0].value
        name = sheet[row][1].value
        category = sheet[row][2].value
        quantity = sheet[row][3].value
        cost = sheet[row][4].value
        value += f"""{str(date_sale)[:11]} {name} {category} {quantity} {cost}\n"""
    return value

wb = open_exel("BD.xlsx")
print(output_sheet(wb))