budget = float(input())
video_card = int(input())
processor = int(input())
ram_memory = int(input())

price_video_card = video_card * 250
price_processor = (price_video_card * 0.35) * processor
price_ram_memory = (price_video_card * 0.10) * ram_memory

total_price = price_processor + price_ram_memory + price_video_card

if video_card > processor:
    total_price = total_price - total_price * 0.15
if total_price > budget:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")
else:
    print(f"You have {budget - total_price:.2f} leva left!")