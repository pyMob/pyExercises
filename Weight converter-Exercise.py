

weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds? (k or l): ")

if unit == "k":
    weight = weight * 2.205
    unit = "lbs."
    print(f"your weight is: {round(weight)} {unit}")
elif unit == "l":
    weight = weight / 2.205
    unit = "kgs."
    print(f"your weight is: {round(weight)} {unit}")
else:
    print(f"{unit} was not valid")

