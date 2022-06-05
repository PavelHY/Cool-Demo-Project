juri = int(input())

average_grade = 0
counter = 0

presentation_name = input()
while presentation_name != "Finish":
    presentation_average_grade = 0

    for _ in range(1, juri + 1):
        rating = float(input())
        counter += 1
        average_grade += rating
        presentation_average_grade += rating

    print(f"{presentation_name} - {presentation_average_grade / juri:.2f}.")

    presentation_name = input()
print(f"Student's final assessment is {average_grade / counter:.2f}.")
