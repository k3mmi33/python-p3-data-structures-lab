# lib/data_structures.py

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # Return a list of names of each spicy food
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    # Return a list of spicy foods with heat level greater than 5
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    # Print each spicy food in the specified format
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # Return a single spicy food dictionary by cuisine
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  # Return None if no match is found

def print_spiciest_foods(spicy_foods):
    # Print only the spicy foods with heat level greater than 5
    for food in get_spiciest_foods(spicy_foods):
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_average_heat_level(spicy_foods):
    # Calculate and return the average heat level of all spicy foods
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)  # Use integer division for average

def create_spicy_food(spicy_foods, spicy_food):
    # Add a new spicy food to the list and return the updated list
    spicy_foods.append(spicy_food)
    return spicy_foods


