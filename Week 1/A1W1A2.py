tip_rate = 15

local_tax_rate = 21

meal_cost = input("Please enter the cost (format 'Cost of the meal: xy.wz'): ")

meal_slice = meal_cost[17:]

meal_float = float(meal_slice)

tip = meal_float / 100 * tip_rate

tax = meal_float / 100 * local_tax_rate

total = meal_float + tax + tip

print(f"Tax: {tax:.3f}, Tip: {tip:.3f}, Total: {total:.3f}")