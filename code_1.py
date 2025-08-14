import pandas as pd
import os

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Ensure the directory exists at the root level
output_dir = 'data'
os.makedirs(output_dir, exist_ok=True)

# Define the output file path
file_path = os.path.join(output_dir, 'sample_data.csv')
# Save the DataFrame to a CSV file
df.to_csv(file_path, index=False)
# Print the path where the file is saved
print(f"DataFrame saved to {file_path}")

# uncomment the following lines to for different versions of the file
## Adding a new row to df for Version 2
# new_row = {'Name': 'David', 'Age': 28, 'City': 'San Francisco'}
# df.loc[len(df.index)] = new_row

## Adding a new row to df for version 3
# new_row = {'Name': 'Eve', 'Age': 22, 'City': 'Seattle'}
# df.loc[len(df.index)] = new_row