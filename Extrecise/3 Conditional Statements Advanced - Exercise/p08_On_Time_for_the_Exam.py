exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_total_time = exam_hour * 60 + exam_minutes
arrival_total_time = arrival_hour * 60 + arrival_minutes

time_diff = abs(exam_total_time - arrival_total_time)

if arrival_total_time > exam_total_time:
    print("Late")

    if time_diff >= 60:
        hours_late = time_diff // 60
        minutes_Late = time_diff % 60

        print(f"{hours_late}:{minutes_Late:02d} hours after the start")
    else:
        print(f"{time_diff} minutes after the start")

elif arrival_total_time <= exam_total_time and time_diff <= 30:
    print("On Time")

    if time_diff > 0:
        print(f"{time_diff} minutes before the start")
else:
    print("Early")
    if time_diff >= 60:
        hours_early = time_diff // 60
        minutes_early = time_diff % 60

        print(f"{hours_early}:{minutes_early:02d} hours before the start")
    else:
        print(f"{time_diff} minutes before the start")

# exam_hour = int(input())
# arrive_hour = int(input())
# arrive_minute = int(input())

# exam_total_minutes = exam_hour * 60 + exam_minute
# arrive_total_minutes = arrive_hour * 60 + arrive_minute

# if arrive_total_minutes > exam_total_minutes:
   # print("Late")
# elif exam_total_minutes - arrive_total_minutes <= 30:
  # print("On time")
# else:
  # print("Early")

# result = abs(exam_total_minutes - arrive_total_minutes)
# if exam_total_minutes - arrive_total_minutes > 0:
  # if result < 60:
    # print(f"{result} minutes before the start")
   # else:
     # print(f"{result // 60}:{result % 60:02d} hours before the start")
# elif arrive_total_minutes - exam_total_minutes > 0:
  # if result < 60:
   # print(f"{result} minutes after the start")
    # else:
     # print(f"{result // 60}:{result % 60:02d} hours after the start")
