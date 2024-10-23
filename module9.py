import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into a pandas DataFrame
file_path = r'c:/Users/balla/Documents/Upenn/Upenn_mod9/AsgnBA3-dataset.csv'
df = pd.read_csv(file_path)
# View the first 5 rows of the DataFrame
print(df.head())

# Check the DataFrame structure, column names, and data types
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Remove rows with missing values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# Get summary statistics
print(df.describe())

# Check value counts for a specific column
print(df['column_name'].value_counts())  # Replace 'column_name' with your actual column name

# Filter rows based on a condition
filtered_df = df[df['column_name'] > some_value]  # Replace 'column_name' and 'some_value' accordingly
print(filtered_df)

# Histogram of a specific column
plt.figure(figsize=(10,6))
sns.histplot(df['numeric_column'], bins=20)
plt.title('Distribution of numeric_column')
plt.show()

# Save to a new CSV file
df.to_csv('cleaned_data.csv', index=False)
