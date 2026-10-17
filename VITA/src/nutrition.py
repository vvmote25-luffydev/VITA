"""Food nutrition data and calculations used by Euron.

Nutrition and price figures are illustrative estimates, not medical advice.
Food calculator values are approximate per 100 grams.
"""

FOOD_NUTRITION = {
    "apple": {"calories": 52, "protein": 0.3, "carbs": 13.8, "fat": 0.2},
    "bread": {"calories": 265, "protein": 9.0, "carbs": 49.0, "fat": 3.2},
    "broccoli": {"calories": 34, "protein": 2.8, "carbs": 6.6, "fat": 0.4},
    "carrot": {"calories": 41, "protein": 0.9, "carbs": 9.6, "fat": 0.2},
    "chicken": {"calories": 239, "protein": 27.0, "carbs": 0.0, "fat": 14.0},
    "egg": {"calories": 155, "protein": 13.0, "carbs": 1.1, "fat": 11.0},
    "orange": {"calories": 47, "protein": 0.9, "carbs": 11.8, "fat": 0.1},
    "paneer": {"calories": 265, "protein": 18.3, "carbs": 1.2, "fat": 20.8},
    "pizza": {"calories": 266, "protein": 11.0, "carbs": 33.0, "fat": 10.0},
    "rice": {"calories": 130, "protein": 2.7, "carbs": 28.0, "fat": 0.3},
    "spinach": {"calories": 23, "protein": 2.9, "carbs": 3.6, "fat": 0.4},
    "tomato": {"calories": 18, "protein": 0.9, "carbs": 3.9, "fat": 0.2},
    "yogurt": {"calories": 59, "protein": 10.0, "carbs": 3.6, "fat": 0.4},
}

MEALS = [
    {"name": "Oats with milk", "category": "breakfast", "calories": 300, "protein": 12, "carbs": 45, "fat": 8, "cost": 35, "vegetarian": True, "hostel_friendly": True, "ingredients": ["oats", "milk"], "method": "kettle_or_microwave"},
    {"name": "Poha with peanuts", "category": "breakfast", "calories": 300, "protein": 8, "carbs": 45, "fat": 10, "cost": 30, "vegetarian": True, "hostel_friendly": False, "ingredients": ["poha", "peanuts", "onion"], "method": "stovetop"},
    {"name": "Vegetable upma", "category": "breakfast", "calories": 280, "protein": 7, "carbs": 42, "fat": 9, "cost": 30, "vegetarian": True, "hostel_friendly": False, "ingredients": ["semolina", "vegetables"], "method": "stovetop"},
    {"name": "Boiled eggs and toast", "category": "breakfast", "calories": 280, "protein": 18, "carbs": 28, "fat": 10, "cost": 35, "vegetarian": False, "hostel_friendly": True, "ingredients": ["egg", "bread"], "method": "kettle_or_microwave"},
    {"name": "Yogurt with oats", "category": "breakfast", "calories": 270, "protein": 14, "carbs": 38, "fat": 6, "cost": 35, "vegetarian": True, "hostel_friendly": True, "ingredients": ["yogurt", "oats"], "method": "no_cook"},
    {"name": "Rice, dal and vegetables", "category": "lunch", "calories": 450, "protein": 16, "carbs": 75, "fat": 9, "cost": 65, "vegetarian": True, "hostel_friendly": False, "ingredients": ["rice", "dal", "vegetables"], "method": "stovetop"},
    {"name": "Chapati, paneer and vegetables", "category": "lunch", "calories": 500, "protein": 22, "carbs": 55, "fat": 18, "cost": 85, "vegetarian": True, "hostel_friendly": False, "ingredients": ["chapati", "paneer", "vegetables", "milk"], "method": "stovetop"},
    {"name": "Rajma rice", "category": "lunch", "calories": 450, "protein": 16, "carbs": 75, "fat": 8, "cost": 60, "vegetarian": True, "hostel_friendly": False, "ingredients": ["rajma", "rice"], "method": "stovetop"},
    {"name": "Chicken, rice and vegetables", "category": "lunch", "calories": 500, "protein": 32, "carbs": 60, "fat": 12, "cost": 100, "vegetarian": False, "hostel_friendly": False, "ingredients": ["chicken", "rice", "vegetables"], "method": "stovetop"},
    {"name": "Chickpea salad with bread", "category": "lunch", "calories": 420, "protein": 16, "carbs": 65, "fat": 9, "cost": 55, "vegetarian": True, "hostel_friendly": True, "ingredients": ["chickpeas", "tomato", "cucumber", "bread"], "method": "no_cook"},
    {"name": "Apple and almonds", "category": "snacks", "calories": 200, "protein": 5, "carbs": 25, "fat": 11, "cost": 30, "vegetarian": True, "hostel_friendly": True, "ingredients": ["apple", "almonds"], "method": "no_cook"},
    {"name": "Yogurt and nuts", "category": "snacks", "calories": 180, "protein": 10, "carbs": 15, "fat": 8, "cost": 30, "vegetarian": True, "hostel_friendly": True, "ingredients": ["yogurt", "nuts", "milk"], "method": "no_cook"},
    {"name": "Roasted chana", "category": "snacks", "calories": 150, "protein": 7, "carbs": 23, "fat": 3, "cost": 15, "vegetarian": True, "hostel_friendly": True, "ingredients": ["chickpeas"], "method": "no_cook"},
    {"name": "Cheese sandwich", "category": "snacks", "calories": 280, "protein": 12, "carbs": 30, "fat": 12, "cost": 40, "vegetarian": True, "hostel_friendly": True, "ingredients": ["bread", "cheese", "milk"], "method": "no_cook"},
    {"name": "Chapati, dal and vegetables", "category": "dinner", "calories": 400, "protein": 15, "carbs": 60, "fat": 10, "cost": 55, "vegetarian": True, "hostel_friendly": False, "ingredients": ["chapati", "dal", "vegetables"], "method": "stovetop"},
    {"name": "Paneer and chapati", "category": "dinner", "calories": 450, "protein": 22, "carbs": 45, "fat": 18, "cost": 75, "vegetarian": True, "hostel_friendly": False, "ingredients": ["paneer", "chapati", "milk"], "method": "stovetop"},
    {"name": "Egg curry and rice", "category": "dinner", "calories": 450, "protein": 20, "carbs": 55, "fat": 15, "cost": 65, "vegetarian": False, "hostel_friendly": False, "ingredients": ["egg", "rice"], "method": "stovetop"},
    {"name": "Chicken and rice", "category": "dinner", "calories": 480, "protein": 32, "carbs": 55, "fat": 12, "cost": 90, "vegetarian": False, "hostel_friendly": False, "ingredients": ["chicken", "rice"], "method": "stovetop"},
    {"name": "Microwave potato with yogurt", "category": "dinner", "calories": 350, "protein": 12, "carbs": 58, "fat": 7, "cost": 40, "vegetarian": True, "hostel_friendly": True, "ingredients": ["potato", "yogurt", "milk"], "method": "kettle_or_microwave"},
]

 
def find_food(food_name):
    """Return an exact food key, allowing case/space differences."""
    if not isinstance(food_name, str):
        return None
    name = food_name.strip().lower()
    return name if name in FOOD_NUTRITION else None


def calculate_nutrition(food, grams):
    """Calculate estimated nutrition for a portion in grams."""
    food_key = find_food(food)
    if food_key is None:
        raise ValueError(f"Unknown food: {food!r}")
    try:
        grams = float(grams)
    except (TypeError, ValueError) as exc:
        raise ValueError("Portion size must be a number.") from exc
    if grams <= 0:
        raise ValueError("Portion size must be greater than zero.")
    factor = grams / 100.0
    return {nutrient: value * factor for nutrient, value in FOOD_NUTRITION[food_key].items()}
