# Task 1: Grocery Store Math 
# Calculate the total cost of three items you'd commonly find in a grocery store, given their individual prices. 
# For example, what would be the cost of bread, peanut butter, and jelly be? Prices don't need to be realistic!

bread_cost = 4.99
peanut_butter_cost = 7.49
jelly_cost = 5.49

print(f"the total cost of bread, peanut butter, & jelly is ${bread_cost + peanut_butter_cost + jelly_cost}")


# Task 2: Bank Interest 
# If you have a savings account with a particular initial amount and a fixed yearly interest rate, 
# calculate the total amount in your account after a year. 
# So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. 
# For the example the expected outcome would be $10,700.

from decimal import Decimal

savings_account_balance = 10000
interest_rate = 0.07 / 365
year = 365

print(f"at the end of the year I'll have ${int(savings_account_balance + (savings_account_balance * (interest_rate * year)))} in my savings account")