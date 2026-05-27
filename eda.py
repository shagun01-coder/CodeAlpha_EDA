import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Student': ['A', 'B', 'C', 'D', 'E'],
    'Marks': [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nStatistics:")
print(df.describe())

plt.bar(df['Student'], df['Marks'])
plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()