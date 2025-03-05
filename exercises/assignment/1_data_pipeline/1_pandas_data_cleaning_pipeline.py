import pandas as pd
import os

os.makedirs('data/pandas_cleaned_data',exist_ok=True)
read_dir = "data/given_data/train.csv"
target_dir = "data/pandas_cleaned_data/data.csv"

try:
    df = pd.read_csv(read_dir)
except FileNotFoundError:
    print(f"Error: The file {read_dir} was not found.")
    exit(1)
except pd.errors.EmptyDataError:
    print(f"Error: The file {read_dir} is empty.")
    exit(1)
except pd.errors.ParserError:
    print(f"Error: There was an issue parsing {read_dir}.")
    exit(1)


print("\n Dataset Info :")
print(df.info())

print(f"\nShape of the Given Dataset is {df.shape}")

print("\n Missing Values:")
print(df.isnull().sum())

print("Filling missing Postal Code with 'N/A' (convert to string)")
df['Postal Code'] = df['Postal Code'].fillna('N/A').astype(str)

print("\n Missing Values after cleaning:")
print(df.isnull().sum())


print(f"\n Duplicate Rows Found: {df.duplicated().sum()}")

if df.duplicated().sum() == 0:
    print("There are No Duplicate Rows in the Data")

else:
    df = df.drop_duplicates(keep='first')
    print("Duplicate Rows Removed")

print("\n Data Type Issues:")
print(df.dtypes)

print("\nConverting Date Columns")
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y', errors='coerce')  
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y', errors='coerce')

#Checking for Invalid Dates
invalid_dates = df[df['Order Date'].isna() | df['Ship Date'].isna()]
if not invalid_dates.empty:
    print(f"\n⚠️ Warning: {len(invalid_dates)} rows have invalid dates!")


print("\nConverting Essential Columns to 'Category' Type")
category_columns = ['Ship Mode', 'Segment','Category', 'Sub-Category']
df[category_columns] = df[category_columns].astype('category')

print("\n Final Dataset After Cleaning:")
print(df.info())

df.to_csv(target_dir, index=False)

