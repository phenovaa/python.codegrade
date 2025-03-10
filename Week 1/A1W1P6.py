days_input = input("Days: ")

days_int = int(days_input)

hours = days_int * 24
minutes = days_int * 1440
seconds = days_int * 86400

print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")