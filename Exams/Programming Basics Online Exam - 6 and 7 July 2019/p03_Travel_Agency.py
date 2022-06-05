citi = input()
packet_tape = input()
vip = input()
days = int(input())

total_price = 0

if days > 7:
    days -= 1
if not (citi in ("Bansko", "Borovets") and packet_tape in ("noEquipment", "withEquipment",)) and not (
        citi in ("Varna", "Burgas") and packet_tape in ("noBreakfast", "withBreakfast")):
    print(f'Invalid input!')
elif days < 1:
    print(f'Days must be positive number!')
else:
    if citi == "Bansko" or citi == "Borovets":
        if packet_tape == "withEquipment":
            total_price = days * 100
            if vip == "yes":
                total_price = total_price - total_price * 0.10

        elif packet_tape == "noEquipment":
            total_price = days * 80
            if vip == "yes":
                total_price = total_price - total_price * 0.05

    elif citi == "Varna" or citi == "Burgas":
        if packet_tape == "withBreakfast":
            total_price = days * 130
            if vip == "yes":
                total_price = total_price - total_price * 0.12

        elif packet_tape == "noBreakfast":
            total_price = days * 100
            if vip == "yes":
                total_price = total_price - total_price * 0.07

    print(f"The price is {total_price:.2f}lv! Have a nice time!")
