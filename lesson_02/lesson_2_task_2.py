def is_year_leap(year):
    return True if year % 4 == 0 else False


result = is_year_leap(2024)
print(f"Год 2024: {result}")
