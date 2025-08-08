import pandas as pd

# Read The Excel file
df = pd.read_excel('testing_file.xlsx')

# Extract only the first word
df['First Name'] = df['First Name'].apply(lambda x: str(x).strip().split()[0])

# Load the mapping file (should contain Arabic names and gender)
gender_df = pd.read_excel(r'C:\Users\Joseph\Desktop\python_project\mapping_file.xlsx') # Adjust the path as necessary

# Create a dictionary for fast lookup
name_gender_map = dict(zip(gender_df['First Name'], gender_df['Gender']))

# Fill Gender only if missing (made it using if else to make it more understandable)
def fill_missing_gender(row):
    if pd.isna(row['Gender']):
        return name_gender_map.get(row['First Name'], None)
    else:
        return row['Gender']

# Apply filling
df['Gender'] = df.apply(fill_missing_gender, axis=1)

# Clean up
#df.drop(columns=['First Name'], inplace=True)

# Save result
df.to_excel('with_gender_filled.xlsx', index=False)

print("--------------------successfully filled------------------------")
