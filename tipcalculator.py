print("Welcome to the tip calculator")
bill=float(input("What was the total bill? "))
tip=float(input("How much tip would you like to give? 10,12 or 15" ))
people=int(input("How many people to split the bill? "))
total_bill=tip/100*bill+bill
each_person=round(total_bill/people,2)
print(f"Each person should give: ${each_person}")
