import pandas as pd

# Specify the path to your text file
text_file_path = 'C:/Users/HP/Desktop/EMAIL.txt'

# Read the text file
with open(text_file_path, 'r') as file:
    data = [line.strip() for line in file if line.strip()]

# Create a DataFrame
df = pd.DataFrame({
    'Sr Number': range(1, len(data) + 1),
    'Email': data
})

# Save to Excel
excel_file_path = 'txt-converted.xlsx'
df.to_excel(excel_file_path, index=False)
print(f"Excel file saved at {excel_file_path}")
