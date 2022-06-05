tax = float(input())

shoes = tax - (tax * 0.40)
outfit = shoes - (shoes * 0.20)
ball = outfit * 0.25
accessories = ball * 0.20

total_price = shoes + outfit + ball + accessories + tax

print(total_price)