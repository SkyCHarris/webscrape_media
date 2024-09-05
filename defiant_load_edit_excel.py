import openpyxl

wb = openpyxl.load_workbook('test.xlsx')
print(wb.sheetnames)

# Create new sheet
wb.create_sheet('Sheet2')
wb.save('test.xlsx')

# # Create new sheet at desired index (place in sheet list)
wb.create_sheet('First Sheet', 0)   # 0 is the sheet index
wb.save("sample.xlsx")