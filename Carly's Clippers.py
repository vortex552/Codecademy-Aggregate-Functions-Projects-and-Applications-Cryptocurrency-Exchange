#below are the collected data
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#sets total price to 0
total_price = 0

#calculates the current total price
for price in prices:
    total_price += price

#prints out the calculated current total price
print("Total Price: $" + str(total_price))

#calculates the current average price 
average_price = total_price / len(prices)

#pints out the the current average price
print("Average Haircut Price: $" + str(average_price))

#deductes 5 from the previous prices and sets them to the varibable 'new_prices'
new_prices = [price - 5 for price in prices]

#prints out the the new prices
print("New Prices: " + str(new_prices))

#sets the total revenue to 0
total_revenue = 0 

#calculates the total revenue by calculating the product of the prices and last weeks sold haircuts
for i in range(len(hairstyles)): 
    total_revenue += prices[i] * last_week[i]

#prints out the total revenue
print("Total Revenue: $" + str(total_revenue))

#calculates the average daily revenue over the past 7 days
average_daily_revenue = total_revenue / 7

#prints out the average dialy revenue over the past 7 days
print("Average Daily Revenue: $" + str(average_daily_revenue))

#so if I am not mistaken hairstyles[i] refers to each individual hairstyle
#i refers to the new_prices
#range(len(new_prices)) counts the number of new_prices and makes it count from 0 to the number of new_prices
#new_prices[i] < 30 stets a condition that these haircuts are only to be listed when they are under $30
cuts_under_30 = [hairstyles[hairstyle] for hairstyle in range(len(hairstyles)) if new_prices[hairstyle] < 30]

#prints out the cuts under $30
print("Cuts Under $30: " + str(cuts_under_30))