transactions_aed = [23.45, 67.89, 12.34, 78.90, 54.21, 11.34]

transactions_usd = []

for item in transactions_aed:
    item_usd = item * 0.27
    print("converting value", item)
    transactions_usd.append(item_usd)

lst = [2, 4, 5, 6]

for number in lst: 
    if number % 2 == 0:
        print(number * 2) 
print(transactions_usd)
