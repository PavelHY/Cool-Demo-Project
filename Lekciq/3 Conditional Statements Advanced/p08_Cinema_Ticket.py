weak_day = input()

price = 0

if weak_day == "Monday":
    price = 12
elif weak_day == "Tuesday":
    price = 12
elif weak_day == "Wednesday":
    price = 14
elif weak_day == "Thursday":
    price = 14
elif weak_day == "Friday":
    price = 12
elif weak_day == "Saturday":
    price = 16
elif weak_day == "Sunday":
    price = 16

print(price)
