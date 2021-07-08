while True:
    months, down_payment, amount, n_depreciation_records = input().split()

    months = int(months)

    if months < 0:
        break

    amount = float(amount)
    down_payment = float(down_payment)
    n_depreciation_records = int(n_depreciation_records)

    depreciation_records = []
    for i in range(n_depreciation_records):
        m, rate = input().split()
        depreciation_records.append((int(m), float(rate)))

    rates = [0] * (months + 1)
    for m, rate in depreciation_records:
        rates[m] = rate

    for i, r in enumerate(rates):
        if not r:
            rates[i] = rates[i - 1]

    owes = amount
    car_value = (amount + down_payment) * (1.0 - rates[0])
    
    payment = amount / months

    months_counter = 0

    while car_value < owes:
        months_counter += 1

        owes -= payment
        car_value *= (1.0 - rates[months_counter])

    print(months_counter, 'months' if months_counter != 1 else 'month')
