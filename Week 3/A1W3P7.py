def truth_tables():
    truth_tables = [True, False]

    for a in truth_tables:
        for b in truth_tables:
            print(f"{a} + {b} = {a and b}")

    for c in truth_tables:
        for d in truth_tables:
            print(f"{c} + {d} = {c or b}")

truth_tables()