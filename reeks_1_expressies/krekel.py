aantal_tjirps_per_minuut = float(input())

temp_f = 50 + (aantal_tjirps_per_minuut - 40) / 4
temp_c = 10 + (aantal_tjirps_per_minuut - 40) / 7

print(f"temperatuur (Fahrenheit): {temp_f}\ntemperatuur (Celsius): {temp_c}")
