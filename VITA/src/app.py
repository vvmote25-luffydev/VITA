"""Main interactive menu for Euron."""

from src.analyzer import analyze_food, show_food_list
from src.meal_planner import create_single_day_plan, create_weekly_plan


def run_app():
    while True:
        print("\n" + "=" * 52)
        print("          EURON FOOD & NUTRITION PLANNER")
        print("=" * 52)
        print("1. Analyze nutrition for a food portion")
        print("2. Create a one-day meal plan")
        print("3. Create a 7-day meal plan")
        print("4. AI food image recognition (optional)")
        print("5. Show foods in the nutrition calculator")
        print("6. Exit")
        choice = input("\nChoose an option (1-6): ").strip()

        if choice == "1":
            analyze_food()
        elif choice == "2":
            create_single_day_plan()
        elif choice == "3":
            create_weekly_plan()
        elif choice == "4":
            from src.image_recognition import recognize_food_image
            recognize_food_image()
        elif choice == "5":
            show_food_list()
        elif choice == "6":
            print("\nThanks for using Euron. Stay healthy!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
