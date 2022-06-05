groups_num = int(input())

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_ppl = 0

for _ in range(1, groups_num + 1):
    people_num = int(input())
    total_ppl += people_num

    if people_num <= 5:
        musala += people_num
    elif 6 <= people_num <= 12:
        monblan += people_num
    elif 13 <= people_num <= 25:
        kilimanjaro += people_num
    elif 26 <= people_num <= 40:
        k2 += people_num
    elif people_num >= 41:
        everest += people_num

total_ppl = musala + monblan + kilimanjaro + k2 + everest

print(f'{musala / total_ppl * 100:.2f}%')
print(f'{monblan / total_ppl * 100:.2f}%')
print(f'{kilimanjaro / total_ppl * 100:.2f}%')
print(f'{k2 / total_ppl * 100:.2f}%')
print(f'{everest / total_ppl * 100:.2f}%')
