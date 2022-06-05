fruit = input()
weak_day = input()
quantity = float(input())

price = 0

if fruit == "banana" or fruit == "apple" or fruit == "orange" or fruit == "grapefruit" or fruit == "kiwi" or fruit == "pineapple" or fruit == "grapes":
    if weak_day == "Saturday" or weak_day == "Sunday":
        if fruit == "banana":
            price = quantity * 2.7
        elif fruit == "apple":
            price = quantity * 1.25
        elif fruit == "orange":
            price = quantity * 0.90
        elif fruit == "grapefruit":
            price = quantity * 1.60
        elif fruit == "kiwi":
            price = quantity * 3.00
        elif fruit == "pineapple":
            price = quantity * 5.60
        elif fruit == "grapes":
            price = quantity * 4.20
        print(f"{price:.2f}")
    elif weak_day == "Monday" or weak_day == "Tuesday" or weak_day == "Wednesday" or weak_day == "Thursday" or weak_day == "Friday":
        if fruit == "banana":
            price = quantity * 2.50
        elif fruit == "apple":
            price = quantity * 1.20
        elif fruit == "orange":
            price = quantity * 0.85
        elif fruit == "grapefruit":
            price = quantity * 1.45
        elif fruit == "kiwi":
            price = quantity * 2.70
        elif fruit == "pineapple":
            price = quantity * 5.50
        elif fruit == "grapes":
            price = quantity * 3.85
        print(f"{price:.2f}")
    else:
        print("error")
else:
    print("error")
