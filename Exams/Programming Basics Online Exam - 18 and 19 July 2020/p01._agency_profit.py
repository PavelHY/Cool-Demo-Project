air_company = input()
adults_ticket = int(input())
kids_ticket = int(input())
price_net = float(input())
tax_price = float(input())

kids_ticket_price_and_tax = (price_net - (price_net * 0.70)) + tax_price
adults_ticket_and_tax = price_net + tax_price

total_money = kids_ticket * kids_ticket_price_and_tax + adults_ticket_and_tax * adults_ticket

profit = total_money * 0.20
print(f"The profit of your agency from {air_company} tickets is {profit:.2f} lv.")