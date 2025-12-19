"""
- You have $50
- You buy an item that is $15
- With a tax of 3%
- print how much money is left
"""

money = 50
item_cost = 15
tax_percent = 0.03
price = item_cost + (item_cost * tax_percent)
print(f"Item cost: {item_cost}")
print(f"Price: {price}")

money_left = money - price
print(f"Total money left: {money_left}")