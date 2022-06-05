move = input()

standard_cnt = 0
student_cnt = 0
kids_cnt = 0
total_tickets = 0

while move != "Finish":
    free_seats = int(input())
    counter_tickets = 0

    while True:
        ticket_tape = input()
        # free_seats = int(input())
        if ticket_tape == "End":
            break
        elif ticket_tape == "standard":
            standard_cnt += 1
            counter_tickets += 1
        elif ticket_tape == "student":
            student_cnt += 1
            counter_tickets += 1
        elif ticket_tape == "kid":
            kids_cnt += 1
            counter_tickets += 1
        total_tickets += 1

        if counter_tickets >= free_seats:
            break
    print(f"{move} - {counter_tickets / free_seats * 100:.2f}% full.")

    move = input()

print(f"Total tickets: {total_tickets}")
print(f"{student_cnt / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_cnt / total_tickets * 100:.2f}% standard tickets.")
print(f"{kids_cnt / total_tickets * 100:.2f}% kids tickets.")
