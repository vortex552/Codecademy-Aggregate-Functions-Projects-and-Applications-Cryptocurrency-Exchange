hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

new_prices = [price - 5 for price in prices]

cuts_under_30 = 0

cuts_under_30 = [hairstyles[hairstyle] for hairstyle in range(len(hairstyles)) if new_prices[hairstyle] < 30]

print(cuts_under_30)

#the code below produces the same output as the above

under_30_hairstyles = list
under_30_hairstyles = []
i = 0
while i < len(hairstyles):
    if (new_prices[i] < 30):
        under_30_hairstyles.append(hairstyles[i])
        i = i + 1
    else:
        i = i + 1

print(under_30_hairstyles)