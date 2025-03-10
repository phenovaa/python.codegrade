years_full_string = input("Enter (Format Example: Years: 2): ")

years_slice_string = years_full_string[7:8]

years_int = int(years_slice_string)

days = years_int * 365 
months = years_int * 12

print(f"Months: {months}, Days: {days}")