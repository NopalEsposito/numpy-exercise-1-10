import numpy as np

#Retail Store Performance & Outlier Analyzer.
#A month of sales data for 5 different store branches. Each branch has 30 days of revenue data.

rng = np.random.default_rng()

#generate data
sales_data = rng.uniform(1000, 5000, size=(5, 30))

#first 2 days,generate to 0.
sales_data[:, :2]=0

#clean data
global_average = np.mean(sales_data)
clean_data = np.where(sales_data / global_average)

#total revenue
store_totals = sales_data.sum(axis=1).reshape(-1, 1)
contribution = sales_data / store_totals

#high performers
high_performer = sales_data[sales_data > 4500]

#the highest data
the_highest_data = np.argmax(sales_data)


print(sales_data)
print(clean_data)
print(contribution)
print(high_performer)
print(the_highest_data)