"""Terminal functions for looking up foods and calculating nutrition."""

from src.nutrition import FOOD_NUTRITION, calculate_nutrition, find_food


def show_food_list():
    print("\nAvailable foods (approximate values per 100 g):")
    print(", ".join(sorted(FOOD_NUTRITION)))


def _read_positive_grams():
    while True:
        raw_value = input("Enter portion size in grams: ").strip()
        try:
            grams = float(raw_value)
            if grams <= 0:
                print("Please enter a value greater than zero.")
                continue
            return grams
        except ValueError:
            print("Please enter a valid number, such as 100 or 150.")


def analyze_food():
    show_food_list()
    food_input = input("\nEnter food name: ").strip()
    food = find_food(food_input)
    if food is None:
        print("Food not found. Please type one of the foods shown above.")
        return

    grams = _read_positive_grams()
    result = calculate_nutrition(food, grams)
    print("\n" + "=" * 40)
    print("          FOOD NUTRITION REPORT")
    print("=" * 40)
    print(f"Food:       {food.title()}")
    print(f"Portion:    {grams:g} g")
    print(f"Calories:   {result['calories']:.1f} kcal")
    print(f"Protein:    {result['protein']:.1f} g")
    print(f"Carbs:      {result['carbs']:.1f} g")
    print(f"Fat:        {result['fat']:.1f} g")
    print("=" * 40)
    print("These are estimates; preparation and brands affect nutrition.")
