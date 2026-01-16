import pandas as pd
import numpy as np

def create_sample_data():
    """Creates a dummy dataset for demonstration."""
    data = {
        'Name': ['  John Doe  ', 'Jane Smith', 'Bob Brown', 'Jane Smith', 'Alice White'],
        'Age': ['28', '34', 'None', '34', '29'],
        'Salary': [50000, 62000, 45000, 62000, np.nan],
        'Join_Date': ['2020-01-15', '2019/05/20', '2021-08-10', '2019/05/20', 'invalid_date'],
        'Email': ['john@email.com', 'jane@EMAIL.com', 'bob@email.com', 'jane@EMAIL.com', 'alice@email.com']
    }
    return pd.DataFrame(data)

def clean_dataset(df):
    """Runs the cleaning pipeline."""
    print("--- Cleaning Data ---")
    
    # 1. Remove Duplicates
    df = df.drop_duplicates(subset=['Email'], keep='first').copy()
    
    # 2. Handle Missing Values
    df['Age'] = df['Age'].replace('None', np.nan)
    df['Salary'] = df['Salary'].fillna(df['Salary'].median())
    df['Age'] = df['Age'].fillna(0)
    
    # 3. Convert Data Types
    df['Age'] = df['Age'].astype(int)
    df['Join_Date'] = pd.to_datetime(df['Join_Date'], errors='coerce')
    
    # 4. Standardize Text
    df['Name'] = df['Name'].str.strip()
    df['Email'] = df['Email'].str.lower()
    
    return df

if __name__ == "__main__":
    # Load data (In a real project, you would use: df = pd.read_csv('data.csv'))
    df = create_sample_data()
    
    print("Original Data Shape:", df.shape)
    
    # Run cleaning
    df_cleaned = clean_dataset(df)
    
    print("\nCleaned Data:")
    print(df_cleaned)
    
    # Save output
    df_cleaned.to_csv('cleaned_data.csv', index=False)
    print("\nSuccess! Saved to 'cleaned_data.csv'")
