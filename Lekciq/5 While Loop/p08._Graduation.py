name = input()

grades_counter = 0
counter = 0
failed_years = 0

while True:
    annual_grade = float(input())
    counter += 1

    if annual_grade < 4:
        failed_years += 1

        if failed_years == 2:
            print(f"{name} has been excluded at {counter} grade")
            break
        counter -= 1
    else:
        grades_counter += annual_grade

    if counter == 12:
        average_grade = counter / grades_counter

        print(f"{name} graduated. Average grade: {grades_counter / counter:.2f}")
        break

