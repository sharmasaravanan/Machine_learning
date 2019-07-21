import matplotlib.pyplot as plt
import pandas as pd
% matplotlib
inline

df = pd.read_csv('data.csv')
df['Amount'] = df['Amount'].str.replace('$', '').str.replace(',', '')
df['Amount'] = pd.to_numeric(df['Amount'])
print(df.head())

df.shape
df.describe()

# Remove unwanted 
df.drop('BranchName', axis=1, inplace=True)
df.head()

num_bins = 10
plt.hist(df['Amount'], num_bins, normed=1, facecolor='blue', alpha=0.7)
plt.show()

sales_by_month = df.groupby('Month').size()
print(sales_by_month)
# Plotting the Graph
plot_by_month = sales_by_month.plot(title='Monthly Sales', xticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
plot_by_month.set_xlabel('Months')
plot_by_month.set_ylabel('Total Sales')

# By Day
sales_by_day = df.groupby('Day').size()
plot_by_day = sales_by_day.plot(title='Daily Sales', xticks=(range(1, 31)), rot=55)
plot_by_day.set_xlabel('Day')
plot_by_day.set_ylabel('Total Sales')

sales_by_hour = df.groupby('Hour').size()
plot_by_hour = sales_by_hour.plot(title='Hourly Sales', xticks=(range(5, 22)))
plot_by_hour.set_xlabel('Working Hours')
plot_by_hour.set_ylabel('Total Sales')
