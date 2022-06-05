mouve = input()
cinema_hall = input()
tickets_sold = int(input())

total_price = 0

if mouve == "A Star Is Born":
    if cinema_hall == "normal":
        total_price = tickets_sold * 7.50
    elif cinema_hall == "luxury":
        total_price = tickets_sold * 10.50
    elif cinema_hall == "ultra luxury":
        total_price = tickets_sold * 13.50

if mouve == "Bohemian Rhapsody":
    if cinema_hall == "normal":
        total_price = tickets_sold * 7.35
    elif cinema_hall == "luxury":
        total_price = tickets_sold * 9.45
    elif cinema_hall == "ultra luxury":
        total_price = tickets_sold * 12.75

if mouve == "Green Book":
    if cinema_hall == "normal":
        total_price = tickets_sold * 8.15
    elif cinema_hall == "luxury":
        total_price = tickets_sold * 10.25
    elif cinema_hall == "ultra luxury":
        total_price = tickets_sold * 13.25

if mouve == "The Favourite":
    if cinema_hall == "normal":
        total_price = tickets_sold * 8.75
    elif cinema_hall == "luxury":
        total_price = tickets_sold * 11.55
    elif cinema_hall == "ultra luxury":
        total_price = tickets_sold * 13.95

print(f"{mouve} -> {total_price:.2f} lv.")
