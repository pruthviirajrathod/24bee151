import openpyxl

file_name = 'students.xlsx'  # Your Excel file name
wb = openpyxl.load_workbook(file_name)
sheet = wb.active

students_dict = {}

for row in sheet.iter_rows(min_row=2, values_only=True):
    rollno, name, marks1, marks2, marks3 = row
    total = ma
