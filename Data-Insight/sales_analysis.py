import pandas as pd
import matplotlib.pyplot as plt

####### Loading Data/File #######
d_f = pd.read_csv('10000 sales records.csv')
#print(d_f.head(10))

## Getting the headers 
headers = d_f.columns
# print(headers)
# print(d_f.describe())


####### Working with the loaded Data  #######

## Q1: Which columns(Country) has the highest(most) sales
"""
    To get the highest sales you need to multiply 
    the quantity with the price per unit
"""
country_HighestSales = d_f.groupby('Country').max()[['Units Sold']]
#print(country_HighestSales)
country_HighestSales.to_excel('Countries with their sales.xlsx')


## Getting the country with highest Cost Price
totalCP = d_f['Total Cost'].max()
countryTCP = d_f.loc[d_f['Total Cost'] == totalCP]
#print(countryTCP)


## Q2: Which columns(Month) has the highest sales
"""
    To get the Month with the highest sales you need
    to get the months and sum up each month
"""

## Adding the month column and Getting the highest sales
"""Converting the column to datetime format and adding Month column"""

d_f['Ship Date'] = pd.to_datetime(d_f['Ship Date'])
d_f['Order Date'] = pd.to_datetime(d_f['Order Date'])
d_f['Month'] = d_f['Order Date'].dt.strftime('%m')
d_f['Year'] = d_f['Order Date'].dt.strftime('%Y')
#print(d_f.head(10))
#print(d_f.iloc[0])
#print(d_f.iloc[2])

"The (groupby()) method/function is used to sort by a column"
month_HighestSales = d_f.groupby('Month').sum()[['Units Sold', 'Total Cost', 'Total Revenue', 'Total Profit']]
#print(month_HighestSales)
#month_HighestSales.to_csv('Months and their sales.csv')


## Q3: What is the most effective sales channel
""" 
    Find the channel with highest number of sales 
    To get the most effective sales channel you have to groupby the sales channel column
"""

no_of_time_online = len(d_f[d_f['Sales Channel'] == 'Online'])
no_of_time_offline = len(d_f[d_f['Sales Channel'] == 'Offline'])
#print(f'Len of online = {no_of_time_online} \n len of offline = {no_of_time_offline}')
sale_cha = d_f.groupby('Sales Channel').sum()[['Units Sold', 'Total Cost', 'Total Revenue', 'Total Profit']]
sale_cha['Total Count'] = [no_of_time_offline, no_of_time_online]
#print(sale_cha)
#sale_cha.to_csv('Most effective sales channel.csv')


## Q4: Which product is the most sold
""" 
    Find the product with highest number of sales 
    To get the most sold product, you have to groupby the product column
"""
item_sale = d_f.groupby('Item Type').sum()[['Units Sold', 'Total Cost', 'Total Revenue', 'Total Profit']]
product_most = item_sale.loc[item_sale['Units Sold'] == item_sale['Units Sold'].max()]
#print(product_most)
#item_sale.to_excel('Items and Sales.xlsx')


## Q5: Which country and region buys the most sold product
""" 
    Find and get the most sold product 
    To get the country and region, you have to locate and stort by the coutry, region column
    Created a new dataframe and made a group from it
"""

""" To get product name, we need to filter by units sold, then get the index of the row and item(product)"""
max_unit = item_sale.loc[item_sale['Units Sold'] == item_sale.iloc[9][0]]
#print(max_unit)

country_item_sale = d_f[d_f['Item Type'] == 'Personal Care'][['Region', 'Country', 'Units Sold', 'Total Cost', 'Total Revenue', 'Total Profit']]
#print(country_item_sale)
p_care = country_item_sale.groupby(['Country', 'Region']).sum()[['Units Sold', 'Total Cost', 'Total Revenue', 'Total Profit']]
# print(p_care)
p_care_limit = p_care.loc[p_care ['Units Sold'] >= 30000]
# print(p_care_limit)
#p_care.to_excel('Countries & regions that buys the most sold product.xlsx')

## Q6: Which country has the highest cost price
country_TCP = country_item_sale.groupby('Country').sum()[['Total Cost']]
#print(country_TCP)
#country_TCP.to_excel('Country and cost price.xlsx')


## Q7 & 8: Which columns(Country)/ (product) has the highest profit 32454798.26

HighestProfit_country = d_f.groupby('Country').sum()[['Total Profit']]
limit_ = HighestProfit_country['Total Profit'].max() - 10000000
top_countryProfit = HighestProfit_country.loc[HighestProfit_country['Total Profit'] >= limit_ ]
#HighestProfit_country.to_excel('country, product and profit.xlsx')

HighestProfit_item =  d_f.groupby('Item Type').sum()[['Total Profit']]
#print(HighestProfit_item)
#HighestProfit_item.to_excel('Product and profit.xlsx')


## Q9: Which columns(Month) has the highest sales
year_sale = d_f.groupby(['Year']).sum()[['Units Sold', 'Total Profit']]
#print(year_sale)
#year_sale.to_excel('yearly sales.xlsx')



## Q10: Which Products were sold together
ordered_together = d_f[d_f['Order ID'].duplicated(keep=False)]
print(ordered_together)



### Visualization Of Data ###

plt.style.use('seaborn')

## V1: Which columns(Country) has the highest(most) sales
# countries = [country for country, df in d_f.groupby('Country')]
# plt.bar(countries,   country_HighestSales['Units Sold'])
# plt.xticks(countries, rotation='vertical', size=8)
# plt.xlabel('Countries')
# plt.ylabel('Unit Sold')
# plt.show()


# ## V2: Which columns(Month) has the highest sales
# months = range(1,13)
# plt.bar(months,   month_HighestSales['Units Sold'])
# plt.xticks(months)
# plt.xlabel('Month')
# plt.ylabel('Unit Sold')
# plt.show()


## V3: What is the most effective sales channel
" In bar; (X-axis, Y-axis)"
# chan = ['Offline', 'Online']
# plt.bar(chan, sale_cha['Units Sold'])
# plt.xticks(chan)
# plt.xlabel('Sales Channel')
# plt.ylabel('Unit Sold')
# plt.show()

## V4: Which product is the most sold
# items = [item for item, df in d_f.groupby('Item Type')]
# plt.bar(items,  item_sale['Units Sold'])
# plt.xticks(items, rotation='vertical', size=8)
# plt.title('Most Sold Product')
# plt.xlabel('Items')
# plt.ylabel('Units Sold')
# plt.grid(True, color='black')
# plt.show()

## V5: Which country and region buys the most sold product
# countryItemSale = [con for con, df in p_care_limit.groupby('Country')]
# plt.bar(countryItemSale,  p_care_limit['Units Sold'])
# plt.xticks(countryItemSale, rotation='vertical', size=8)
# plt.title('Some Countries that buys the most sold product')
# plt.xlabel('Country')
# plt.ylabel('Units Brought')
# plt.grid(True, color='black')
# plt.show()


## V6: Which country has the highest cost price
# countryItemSale = [con for con, df in office_sup_TCP.groupby('Country')]
# plt.bar(countryItemSale,  office_sup_TCP['Total Cost Price'])
# plt.xticks(countryItemSale, rotation='vertical', size=8)
# plt.xlabel('Country')
# plt.ylabel('Total Cost Price', rotation='vertical')
# plt.show()


## V7: Which country has the highest profit
# count_pro = [con for con, df in top_countryProfit.groupby('Country')]
# plt.bar(count_pro,  top_countryProfit['Total Profit'])
# plt.xticks(count_pro, rotation='vertical', size=8)
# plt.title('Country And Profit')
# plt.xlabel('Country')
# plt.ylabel('Total Profit', rotation='vertical')
# plt.grid(True, color='Black')
# plt.show()


## V8: Which item has the highest profit
# _profit = [pro for pro, df in HighestProfit_item.groupby('Item Type')]
# plt.bar(_profit, HighestProfit_item['Total Profit'])
# plt.xticks(_profit, rotation='vertical', size=8)
# plt.title('Products and profit')
# plt.xlabel('Product')
# plt.ylabel('Profit', rotation='vertical')
# plt.grid(True, color='black')
# plt.show()


## V9: Which columns(Month) has the highest sales
# year_ = [year for year, df in d_f.groupby('Year')]
# fig, ax1 = plt.subplots()
# ax1.bar(year_, year_sale['Units Sold'], label='Units Sold')
# ax2 = ax1.twinx()
# ax2.plot(year_, year_sale['Total Profit'],label='Profit', color='red')
#plt.xticks(HighestProfit_item['Unit Cost'], rotation='vertical', size=8)
# ax1.set_title('Year, Sales And Profit')
# ax1.tick_params(axis='y', rotation='auto', labelcolor='blue')
# ax1.set_ylabel('Units Sold', color='blue')
# ax2.tick_params(axis='y', rotation='auto', labelcolor='red')
# ax2.set_ylabel('Profit', color='red')
# ax1.set_xlabel('Year')
# plt.grid(False)
# plt.show()


## V10: Which Products were sold together