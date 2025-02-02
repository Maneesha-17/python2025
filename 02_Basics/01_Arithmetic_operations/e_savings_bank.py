"""
Purpose: Saving Bank

    Initial Balance 0

Algorithm
----------
Step 1: Create a variable 'balance' with intial value 0
Step 2: Initial deposit of min balance 1500
Step 3: Salary credited of 3300
Step 4: Online purchase of 33.33
Step 5: House Rent paid of 1500
Step 6: Display Balance
"""
# constants

BALANCE = 0
INITIAL_DEPOSIT = 1500
SALARY_CREDITED = 3300
ONLINE_PURCHASE =33.33
HOUSE_RENT = 1500

total_balance = (INITIAL_DEPOSIT + SALARY_CREDITED -  
ONLINE_PURCHASE - HOUSE_RENT) 

print("Initial Balance: ", BALANCE)
print("Initial deposit: ", INITIAL_DEPOSIT)
print("Salary Credited: ", SALARY_CREDITED)
print("Online Purchase: ", ONLINE_PURCHASE)
print("House rent: ", HOUSE_RENT)
print("Total Balance  : ", total_balance)

