def celsius_to_fahrenheit():
    celsius = 10
    fahrenheit = 50

    print("°C °F")

    for i in range(10):
        for b in range(1):
            print(celsius, fahrenheit, end=" ")
            celsius += 10
            fahrenheit = (celsius * 9/5) + 32
            fahrenheit = int(fahrenheit)
        print()

print(celsius_to_fahrenheit())