def calculate_calories_container(calories_per_kg, grams_per_container):
    calories_per_container = ((int(calories_per_kg) / 1000)*int(grams_per_container))
    return calories_per_container
