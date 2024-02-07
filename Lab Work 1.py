"""
    Program Purpose: To ask user to input data and calculate the conversion rate of currencies.
    Programmer: MUHAMMAD AFIF NAQIUDDIN BIN OTHMAN
    Date: 7 February 2024
"""
# Exchange Rates for Currencies
print("Exchange rates:")
print("USD - US Dollar: 0.25")
print("EUR - Euro: 0.21")
print("GBP - British Pound: 0.18")
print("SGP - Singapore Dollar: 0.28")

# Prompt the user to choose the target currency.
print("Choose any ONE of the target currency below:")
print("Please type the following number to represent the target currency:")
print("1. USD - US Dollar")
print("2. EUR - Euro")
print("3. GBP - British Pound")
print("4. SGP - Singapore Dollar")

# Input from the user will be assigned to the variable named choice
choice = int(input("Enter your choice (1 or 2 or 3 or 4): "))

# Check the user's choice and perform the conversion accordingly
if choice == 1:
    target_currency = "USD"
    exchange_rate = 0.25
elif choice == 2:
    target_currency = "EUR"
    exchange_rate = 0.21
elif choice == 3:
    target_currency = "GBP"
    exchange_rate = 0.18
elif choice == 4:
    target_currency = "SGP"
    exchange_rate = 0.28
else:
    print("Invalid choice!")
    exit()

# Prompt the user to input the amount in MYR
amount_myr = float(input("Enter the amount in Malaysian Ringgit (MYR): "))

# Calculate the converted amount
converted_amount = amount_myr * exchange_rate

# Display the result
print(f"{amount_myr} MYR is equal to {converted_amount} {target_currency}.")
