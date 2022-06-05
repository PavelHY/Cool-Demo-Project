price_of_the_trip = float(input())
puzzles = float(input())
dolls = float(input())
teddy_bears = float(input())
minions = float(input())
trucks = float(input())

toy_price = puzzles * 2.60 + dolls * 3 + teddy_bears * 4.10 + trucks * 2 + minions * 8.20
toy_num = puzzles + dolls + trucks + teddy_bears + minions

if toy_num >= 50:
    toy_price = toy_price - toy_price * 0.25

toy_price = toy_price - toy_price * 0.10

if price_of_the_trip <= toy_price:
    print(f"Yes! {toy_price - price_of_the_trip:.2f} lv left.")
else:
    print(f"Not enough money! {price_of_the_trip - toy_price:.2f} lv needed.")