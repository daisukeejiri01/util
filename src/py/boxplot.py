import seaborn as sns
import matplotlib.pyplot as plt

# Load the sample dataset
tips = sns.load_dataset('tips')

# Use FacetGrid to create a separate boxplot for each group
g = sns.FacetGrid(tips, col='day', col_wrap=2, height=4)  # Create a separate plot for each 'day'
g.map(sns.boxplot, 'time', 'total_bill', order=['Lunch', 'Dinner'])  # Map the boxplot for 'time' vs 'total_bill'

plt.show()  # Display the plots