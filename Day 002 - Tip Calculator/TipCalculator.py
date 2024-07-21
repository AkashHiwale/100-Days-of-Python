bill = float(input("What was the total Bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
split = int(input("How many people to split the bill? "))

if tip == 10:
  bill = bill + bill*0.10
elif  tip == 12:
  bill = bill + bill*0.12
elif  tip == 15:
  bill = bill + bill*0.15
else:
  bill = bill + bill*0.20

one_person_bill = round(bill / split, 2)

print(f"Each person should pay: {one_person_bill}.")
