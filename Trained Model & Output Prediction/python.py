import pandas as pd

# Load train and test data from Excel files
train_data = pd.read_excel("Data.xlsx")
test_data = pd.read_excel("Test Data.xlsx")

print(train_data.head())
