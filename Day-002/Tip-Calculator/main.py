print("Welcome to the top calculator")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split_members = int(input("How many people to split the bill? "))

total_bill = bill + (bill*tip_percentage)/100
per_person_bill = total_bill / split_members

print(f"Each person should pay: ${round(per_person_bill, 2)}")
