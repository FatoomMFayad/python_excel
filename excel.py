import openpyxl as xl

file_name = 'C:/Users/Fatoom/Documents/countries.xlsx'
try:
    wb = xl.load_workbook(file_name)
    sheet = wb.active

    print(sheet.cell(row=1, column=1).value)
    print(sheet['A2'].value)

except FileNotFoundError as e:
    print(e)