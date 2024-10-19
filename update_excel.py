import openpyxl

# Load the existing Excel file
file_path = 'data.xlsx'  # Adjust this path if necessary
workbook = openpyxl.load_workbook(file_path)
sheet = workbook.active

# Example update: Append a new row
new_row = ["New Folder Added", "Details about the folder"]
sheet.append(new_row)

# Save the updated Excel file
workbook.save(file_path)
