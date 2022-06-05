failed_results_num = int(input())

failed_time = 0
solved_problem_count = 0
grade_sum = 0
last_problem = ""
has_failed = True

while failed_time < failed_results_num:
    problem = input()
    if problem == "Enough":
        has_failed = False
        break

    grade = int(input())
    if grade <= 4:
        failed_time += 1
    solved_problem_count += 1
    grade_sum += grade
    last_problem = problem

if has_failed:
    print(f"You need a break, {failed_time} poor grades.")

else:
    print(f"Average score: {grade_sum / solved_problem_count:.2f}")
    print(f"Number of problems: {solved_problem_count}")
    print(f"Last problem: {last_problem}")