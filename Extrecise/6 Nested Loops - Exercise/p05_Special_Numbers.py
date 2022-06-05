n = int(input())

# Thousands
for n1 in range(1, 9 + 1):
    # Hundreds
    for n2 in range(1, 9 + 1):
        # Tens
        for n3 in range(1, 9 + 1):
            # Ones
            for n4 in range(1, 9 + 1):
                is_special = n % n4 == 0 and \
                             n % n3 == 0 and \
                             n % n2 == 0 and \
                             n % n1 == 0

                # whole_number = n1 * 1000 + n2 * 100 + n3 * 10 + n4
                if is_special:
                    print(f'{n1}{n2}{n3}{n4}', end=' ')

