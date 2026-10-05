units = int(input("Enter electricity units: "))
if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = units *4
elif units <= 300:
    bill = units * 6
else:
    bill = units * 8
print("Electricity bill = ",bill)
