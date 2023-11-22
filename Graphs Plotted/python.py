import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('dataset - netflix1.csv')

for column in df.columns:
    df[column] = pd.to_numeric(df[column], errors='coerce')

numeric_columns = df.select_dtypes(include=['number']).columns
print("Numeric Columns:", numeric_columns)

print(df.head())
print(df.describe())

sns.histplot(df['release_year'], bins=20)
plt.title('Histogram of Release Year')
plt.xlabel('Release Year')
plt.ylabel('Frequency')
plt.show()

sns.barplot(x='type', y='release_year', data=df)
plt.title('Bar Plot of Type vs. Release Year')
plt.xlabel('Type')
plt.ylabel('Release Year')
plt.xticks(rotation=45)
plt.show()

sns.scatterplot(x='rating', y='duration', data=df)
plt.title('Scatter Plot of Rating vs. Duration')
plt.xlabel('Rating')
plt.ylabel('Duration')
plt.show()

sns.pairplot(df[numeric_columns])
plt.title('Pair Plot of Numeric Columns')
plt.show()

correlation_matrix = df[numeric_columns].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
