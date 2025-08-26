import os
import pandas as pd

# 1. Create sample data as a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# 2. Convert to DataFrame
df = pd.DataFrame(data)

# adding a new row
new_row={'Name':'john','Age':33,'city':'LA'}
df.loc[len(df.index)]=new_row

# 3. Create 'data' folder if it doesn't exist
os.makedirs('data', exist_ok=True)

# 4. Save the DataFrame to a CSV file in the 'data' folder
csv_path = os.path.join('data', 'temp_dataset.csv')
df.to_csv(csv_path, index=False)

print(f"CSV file saved to {csv_path}")
