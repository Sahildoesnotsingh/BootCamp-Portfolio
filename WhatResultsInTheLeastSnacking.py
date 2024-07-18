import tabulate
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('Python data_analysis-2.py - Sheet1 (2).csv')
 # Load CSV File
correlation_matrix = df.drop('Date', axis=1).corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap', fontsize=14)
plt.show()
