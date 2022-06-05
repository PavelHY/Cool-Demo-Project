favorite_book = input()

book_counter = 0

curr_book = input()
while True:
    if curr_book == 'No More Books':
        print("The book you search is not here!")
        print(f"You checked {book_counter} books.")
        break

    elif curr_book == favorite_book:
        print(f"You checked {book_counter} books and found it.")
        break

    book_counter += 1
    curr_book = input()
