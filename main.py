print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
while tip != 10 and tip != 12 and tip != 15:
    tip = int(input("Please, enter one of three options: 10, 12 or 15? "))

split = int(input("How many people to split the bill? "))

count_tip = bill / 100 * int(tip)
total_bill = count_tip + bill
result = "{:.2f}".format(total_bill / split)

print(f"Each person should pay: ${result}")