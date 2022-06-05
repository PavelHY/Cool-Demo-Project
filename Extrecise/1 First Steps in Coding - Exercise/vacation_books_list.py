import math

num_pages = int(input())
pages_per_day = int(input())
num_day_for_1book = int(input())

total_time_need_for_1book = num_pages / pages_per_day
reading_time_needed_1day = total_time_need_for_1book / num_day_for_1book

print(reading_time_needed_1day)