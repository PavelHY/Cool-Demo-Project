N1 = int(input())
N2 = int(input())
operation = input()

even_or_odd = ""
results = 0
if N1 == 0:
    print(f"Cannot divide {N2} by zero")
elif N2 == 0:
    print(f"Cannot divide {N1} by zero")

if operation == "-":
    results = N1 - N2
    if results % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{N1} {operation} {N2} = {results} - {even_or_odd}")
elif operation == "+":
    results = N1 + N2
    if results % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{N1} {operation} {N2} = {results} - {even_or_odd}")
elif operation == "*":
    results = N1 * N2
    if results % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{N1} {operation} {N2} = {results} - {even_or_odd}")

elif operation == "/" and (N1 != 0 and N2 != 0):
    results = N1 / N2
    print(f"{N1} / {N2} = {results:.2f}")
elif operation == "%" and (N1 != 0 and N2 != 0):
    results = N1 % N2
    print(f"{N1} % {N2} = {results}")


