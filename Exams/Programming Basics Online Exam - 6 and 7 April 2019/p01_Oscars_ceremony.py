rent = int(input())

figurines = rent - rent * 0.30
catering = figurines - figurines * 0.15
sound_system = catering - catering * 0.50

total_price = rent + figurines + catering + sound_system

print(f"{total_price:.2f}")
