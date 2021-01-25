# Use import math to use math functions
import math
# Display the statement below so the user can know their options
print(
    """Please choose either \'Investment\' or \'Boond\' 
    from the menu below to proceed:\n\nInvestment      
    - to calculate the amount of interest you will earn on intrest.\nBond             
    - to calculate the amount you will have to pay on a home loan."""
)

# Request input from user
transaction_type = input("Enter here: ")

if transaction_type.lower().strip(" ") == "investment":
    amount = float(input("Please enter the amount you are depositing: "))
    intrest_rate_percent = float(input("Please enter the intrest rate ,e.g 8 or 10: "))
    num_years = int(input("Please enter the number of years you are investing for: "))
    intrest_type = input('Do you want "Compound" or "Simple" intrest: ')

# Calculate and display answer to user based on what the user has selected
    if intrest_type.lower().strip(" ") == "simple":
        intrest_rate = intrest_rate_percent * 1 / 100
        Accum_amount = amount * (1 + intrest_rate * num_years)
        print(f"The amount you will get after your investment is R{Accum_amount}")

    elif intrest_type.lower().strip(" ") == "compound":
        intrest_rate = intrest_rate_percent * 1 / 100
        Accum_amount = amount * math.pow((1 + intrest_rate), num_years)
        print(f"The amount you will get after your investment is R{Accum_amount}")
    else:
        print(
            'You have entered an invalid option. Please enter "Compound" or "Simple" only: '
        )

# calculate and display the answer here if the user selected "Bond" isntead of "Investment"
elif transaction_type.lower().strip(" ") == "bond":
    house_value = float(
        input("Please enter the present value of the house.E.g 100000: ")
    )
    intrest_rate_percent = float(input("Please enter the intrest rate, e.g 7: "))
    num_months_repaymet = int(
        input("Please enter the number of months you plan to repay the bond.E.g.120: ")
    )

    intrest_rate = intrest_rate_percent / 12

    repayment = house_value / (
        (1 - (1 + (intrest_rate / 100)) ** (-1 * num_months_repaymet)) / (intrest_rate / 100)
    )
    print(f"The amount you will repay each month is R{repayment}")

# Dispaly the following if the user inputs an invalid option
else:
    print(
        'You have entered an invalid option. Please enter "Investment" or "Bond" only:'
    )