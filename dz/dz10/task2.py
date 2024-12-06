def multiplication_table():
    for i in range(1, 11):
        for r in range(1, 11):
            print(f"{i} * {r} = {i * r}")
        print()
multiplication_table()