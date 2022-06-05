change = float(input()) * 100
resto = int(change)
coin_cnt = 0

while resto > 0.00:
    if resto >= 200:
        resto -= 200
    elif resto >= 100:
        resto -= 100
    elif resto >= 50:
        resto -= 50
    elif resto >= 20:
        resto -= 20
    elif resto >= 10:
        resto -= 10
    elif resto >= 5:
        resto -= 5
    elif resto >= 2:
        resto -= 2
    elif resto >= 1:
        resto -= 1
    coin_cnt += 1

print(coin_cnt)

