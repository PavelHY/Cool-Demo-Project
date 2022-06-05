pc_num = int(input())

rating = 0
sells = 0

for i in range(pc_num):
    v_sells = int(input())
    rating_n = v_sells % 10
    sells_n = v_sells // 10
    if v_sells % 10 == 2:
        rating += 2
        sells += 0
    if v_sells % 10 == 3:
        rating += 3
        sells += sells_n * 0.5
    elif v_sells % 10 == 4:
        rating += 4
        sells += sells_n * 0.7
    elif v_sells % 10 == 5:
        rating += 5
        sells += sells_n * 0.85
    elif v_sells % 10 == 6:
        rating += 6
        sells += sells_n * 1

rating_total = rating / pc_num
print(f"{sells:.2f}")
print(f"{rating_total:.2f}")
