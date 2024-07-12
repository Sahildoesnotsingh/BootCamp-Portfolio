#plt.title('Iris Dataset scatterplot')

# showing the plot
#plt.show()
#import matplotlib.pyplot as plt
#import seaborn as sns
#import numpy as np

#tips_df = sns.load_dataset("tips")
#print(tips_df)
#sns.barplot(x="day" , y="total_bill" , hue = 'sex', data=tips_df)
#plt.show()
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
flo_df = sns.load_dataset('iris') #accessing dataset

plt.title('Iris Dataset')
# Calculate the correlation matrix

# Convert the 'species' column to numerical values

flo_df['species'] = pd.factorize(flo_df['species'])[0]

correlation_matrix = flo_df.corr()

# Create a heatmap

sns.heatmap(correlation_matrix, annot=True)

# Display the heatmap

plt.show()
#sns.pairplot(flo_df, hue ='species')
#plt.show()


