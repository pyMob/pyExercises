credit_card = input("Enter your credit card number: ")
last_digits = credit_card[-4:]

if len(credit_card) < 19:
    print(f"Credit card number must be 19 digits.")
elif not credit_card.isalpha:
    print("Please enter a valid credit card number (Remove any alphabetical characters).")
else:
    print(f"The card you'd like to use is: XXXX-XXXX-XXXX-{last_digits} correct? (Y/N): ")
    correct = input("(Y/N): ")

    if correct == "Y":
        print(f"Awesome! We'll use XXXX-XXXX-XXXX-{last_digits} going forward.")
    elif correct == "N":
        print(f"Please enter another form of payment.")
    else:
        print(f"Invalid input. Please enter 'Y' or 'N'.")
