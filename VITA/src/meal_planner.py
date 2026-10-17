"""Rule-based one-day and seven-day meal planner."""

import random
from src.nutrition import MEALS

CATEGORIES = ["breakfast", "lunch", "snacks", "dinner"]


def get_preferences():
    print("\nFood preference:")
    print("1. Vegetarian only")
    print("2. Include vegetarian and non-vegetarian meals")
    vegetarian_choice = input("Choose 1 or 2: ").strip()
    vegetarian = vegetarian_choice != "2"
    if vegetarian_choice not in ("1", "2"):
        print("Invalid choice; using vegetarian meals only.")

    while True:
        try:
            budget = float(input("Daily budget in rupees (example 200): ").strip())
            if budget <= 0:
                raise ValueError
            break
        except ValueError:
            print("Enter a valid budget greater than zero.")

    hostel_answer = input("Use only no-cook/kettle/microwave-friendly meals? (y/n): ").strip().lower()
    hostel = hostel_answer in ("y", "yes")
    print("Enter allergies or foods to avoid, separated by commas.")
    allergy_text = input("Foods to avoid (or press Enter for none): ").strip().lower()
    allergies = [item.strip() for item in allergy_text.split(",") if item.strip()]

    print("Goal: 1. Balanced  2. High-protein  3. Budget-friendly")
    goal_choice = input("Choose 1, 2 or 3: ").strip()
    goal = {"1": "balanced", "2": "high-protein", "3": "budget"}.get(goal_choice, "balanced")
    if goal_choice not in ("1", "2", "3"):
        print("Invalid choice; using balanced meals.")

    return {"vegetarian": vegetarian, "budget": budget, "hostel": hostel,
            "allergies": allergies, "goal": goal}


def filter_meals(category, preferences):
    options = [meal for meal in MEALS if meal["category"] == category]
    if preferences.get("vegetarian", True):
        options = [meal for meal in options if meal["vegetarian"]]
    if preferences.get("hostel", False):
        options = [meal for meal in options if meal["hostel_friendly"] or meal["method"] == "no_cook"]

    allergies = [a.lower() for a in preferences.get("allergies", [])]
    if allergies:
        options = [meal for meal in options if not any(
            allergy in ingredient.lower()
            for allergy in allergies for ingredient in meal["ingredients"]
        )]

    goal = preferences.get("goal", "balanced")
    if goal == "high-protein":
        options.sort(key=lambda meal: (-meal["protein"], meal["cost"]))
    elif goal == "budget":
        options.sort(key=lambda meal: (meal["cost"], -meal["protein"]))
    else:
        # Use a stable name order before random selection so results remain readable.
        options.sort(key=lambda meal: meal["name"])
    return options


def choose_daily_meals(preferences):
    """Choose one meal per category while trying to respect the daily budget."""
    choices_by_category = [filter_meals(category, preferences) for category in CATEGORIES]
    if any(not choices for choices in choices_by_category):
        return None

    # Start with the lowest-cost choice in each category. Then improve according
    # to the selected goal while keeping the total cost within budget when possible.
    selected = [min(options, key=lambda meal: meal["cost"]) for options in choices_by_category]
    budget = preferences.get("budget", float("inf"))
    if preferences.get("goal") == "high-protein":
        candidates = [sorted(options, key=lambda meal: (-meal["protein"], meal["cost"])) for options in choices_by_category]
    elif preferences.get("goal") == "balanced":
        candidates = [sorted(options, key=lambda meal: (abs(meal["calories"] - 350), meal["cost"])) for options in choices_by_category]
    else:
        candidates = [sorted(options, key=lambda meal: (meal["cost"], -meal["protein"])) for options in choices_by_category]

    for index, options in enumerate(candidates):
        current_cost = sum(meal["cost"] for meal in selected)
        for candidate in options:
            proposed_cost = current_cost - selected[index]["cost"] + candidate["cost"]
            if proposed_cost <= budget:
                selected[index] = candidate
                break
    return selected


def show_day(day_number, meals):
    print("\n" + "=" * 58)
    print(f"DAY {day_number}")
    print("=" * 58)
    totals = {"calories": 0, "protein": 0, "carbs": 0, "fat": 0, "cost": 0}
    for meal in meals:
        print(f"{meal['category'].title():10} | {meal['name']} | Rs.{meal['cost']}")
        for key in ("calories", "protein", "carbs", "fat", "cost"):
            totals[key] += meal[key]
    print("-" * 58)
    print(f"Estimated nutrition: {totals['calories']} kcal | Protein {totals['protein']} g | Carbs {totals['carbs']} g | Fat {totals['fat']} g")
    print(f"Estimated food cost: Rs.{totals['cost']} per day")
    return totals


def _plan_is_possible(preferences):
    empty_categories = [category for category in CATEGORIES if not filter_meals(category, preferences)]
    if empty_categories:
        print("\nNo meals matched your filters for: " + ", ".join(empty_categories))
        print("Try changing the food preference, hostel mode, or foods-to-avoid list.")
        return False
    return True


def create_single_day_plan():
    preferences = get_preferences()
    if not _plan_is_possible(preferences):
        return
    meals = choose_daily_meals(preferences)
    if meals is None:
        print("Could not generate a plan with those preferences.")
        return
    totals = show_day(1, meals)
    if totals["cost"] > preferences["budget"]:
        print("Note: Even the selected options exceed your budget; consider increasing it.")
    print("Please verify ingredient labels if you have an allergy.")
    print("This is a general planner, not medical dietary advice.")


def create_weekly_plan():
    preferences = get_preferences()
    if not _plan_is_possible(preferences):
        return
    weekly_cost = 0
    over_budget_days = 0
    print("\nGenerating your 7-day meal plan...")
    for day in range(1, 8):
        meals = choose_daily_meals(preferences)
        if meals is None:
            print("Could not generate a plan with those preferences.")
            return
        totals = show_day(day, meals)
        weekly_cost += totals["cost"]
        if totals["cost"] > preferences["budget"]:
            over_budget_days += 1
    print("\n" + "=" * 58)
    print("WEEKLY SUMMARY")
    print("=" * 58)
    print(f"Estimated weekly food cost: Rs.{weekly_cost}")
    print(f"Your budget: Rs.{preferences['budget']:.2f} per day")
    print(f"Estimated 7-day budget: Rs.{preferences['budget'] * 7:.2f}")
    if over_budget_days:
        print(f"Note: {over_budget_days} day(s) exceeded the daily budget estimate.")
    else:
        print("The plan is within the daily budget estimate.")
    print("Costs and nutrition are estimates. This is not medical dietary advice.")
