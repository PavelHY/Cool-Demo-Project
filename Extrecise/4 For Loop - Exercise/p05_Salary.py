open_tabs = int(input())
salary = float(input())

fine = 0

for i in range(0, open_tabs):
    tab = input()

    if tab == "Facebook":
        fine += 150
    elif tab == "Instagram":
        fine += 100
    elif tab == "Reddit":
        fine += 50
    if salary - fine <= 0:
        break

if salary <= fine: # or salary - fine <= 0:
    print("You have lost your salary.")
else:
    print(f"{round(salary - fine)}")
