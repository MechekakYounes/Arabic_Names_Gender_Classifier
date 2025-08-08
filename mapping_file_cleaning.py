import pandas as pd
import re

# Load the mapping file
gender_df = pd.read_excel(r'C:\Users\Joseph\Desktop\python_project\mapping_file.xlsx')

# Extract the first word only
gender_df['First Name'] = gender_df['First Name'].apply(lambda x: str(x).strip().split()[0])

# Remove names that are written in English (A-Z or a-z only)
gender_df = gender_df[~gender_df['First Name'].str.contains(r'^[A-Za-z]+$|.*\d.*', na=False)]

# Drop duplicates on first name
gender_df = gender_df.drop_duplicates(subset='First Name', keep='first')

# Save cleaned version
gender_df.to_excel('mapping_file5.xlsx', index=False)

print("✅ English names removed and file cleaned using first word only.")
