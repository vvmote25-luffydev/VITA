
from __future__ import annotations

import random
import streamlit as st

from src.nutrition import FOOD_NUTRITION, MEALS, calculate_nutrition
from src.meal_planner import CATEGORIES, filter_meals, choose_daily_meals


st.set_page_config(
    page_title="VITA | Intelligent Nutrition System",
    page_icon="🌿",
    layout="wide",
)
   



st.markdown(
    """
    <style>
        @import url(
            'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap'
        );

        html, body, [class*="css"] {
            font-family: 'DM Sans', sans-serif;
        }

        .stApp {
            background: #f7f8f4;
        }

        [data-testid="stSidebar"] {
            background: #172f27;
        }

        [data-testid="stSidebar"] * {
            color: #f3f7f1 !important;
        }

        [data-testid="stSidebar"] [data-testid="stRadio"] label {
            padding: 7px 10px;
            border-radius: 10px;
        }

        [data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
            background: #29483b;
        }

        .hero {
            padding: 28px 30px;
            border-radius: 22px;
            background: linear-gradient(120deg, #17392e, #285d49);
            color: white;
            margin-bottom: 20px;
        }

        .hero h1 {
            font-family: 'Manrope', sans-serif;
            font-size: 2.25rem;
            line-height: 1.15;
            margin: 0 0 8px 0;
            color: white;
        }

        .hero p {
            color: #d7e7dc;
            margin: 0;
            font-size: 1rem;
        }

        .eyebrow {
            text-transform: uppercase;
            letter-spacing: .15em;
            font-size: .72rem;
            font-weight: 700;
            color: #a9d2b5;
            margin-bottom: 10px;
        }

        .section-title {
            font-family: 'Manrope', sans-serif;
            font-weight: 800;
            font-size: 1.35rem;
            color: #203b30;
            margin: 12px 0 4px 0;
        }

        .muted {
            color: #66776c;
            font-size: .92rem;
        }

        .metric-card {
            background: white;
            border: 1px solid #e3e9e1;
            border-radius: 16px;
            padding: 18px 20px;
            min-height: 112px;
        }

        .metric-label {
            color: #68796e;
            font-size: .85rem;
            margin-bottom: 7px;
        }

        .metric-value {
            color: #1b3c2e;
            font-family: 'Manrope', sans-serif;
            font-size: 1.7rem;
            font-weight: 800;
        }

        .metric-unit {
            color: #738177;
            font-size: .82rem;
            font-weight: 500;
        }

        .meal-card {
            background: white;
            border: 1px solid #e3e9e1;
            border-radius: 14px;
            padding: 15px 16px;
            margin-bottom: 10px;
        }

        .meal-type {
            color: #4d7c5d;
            text-transform: uppercase;
            letter-spacing: .1em;
            font-size: .7rem;
            font-weight: 800;
        }

        .meal-name {
            color: #203b30;
            font-weight: 700;
            font-size: 1.02rem;
            margin: 4px 0;
        }

        .meal-meta {
            color: #66776c;
            font-size: .84rem;
        }

        div.stButton > button[kind="primary"] {
            background: #2c654d;
            border: 0;
            border-radius: 10px;
            color: white;
            font-weight: 700;
        }

        div.stButton > button[kind="primary"]:hover {
            background: #204d3a;
            color: white;
        }

        div[data-testid="stForm"] {
            background: white;
            border: 1px solid #e3e9e1;
            padding: 20px;
            border-radius: 16px;
        }

        /* Improve visibility of labels and radio buttons */

        [data-testid="stMain"] label,
        [data-testid="stMain"] [data-testid="stWidgetLabel"] p,
        [data-testid="stMain"] [data-testid="stMarkdownContainer"] p {
            color: #263b31;
        }

        [data-testid="stMain"] [data-testid="stRadio"] label,
        [data-testid="stMain"] [data-testid="stCheckbox"] label {
            color: #263b31 !important;
            opacity: 1 !important;
        }

        [data-testid="stMain"] [data-testid="stRadio"] div[role="radiogroup"] {
            gap: 12px;
        }

        [data-testid="stMain"] [data-testid="stRadio"] div[role="radiogroup"] label {
            background: #f1f6f1;
            border: 1px solid #cbd9cd;
            border-radius: 10px;
            padding: 8px 13px;
            margin-right: 4px;
            color: #203b30 !important;
        }

        [data-testid="stMain"] [data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) {
            background: #e0efe3;
            border-color: #2c654d;
            color: #17392e !important;
        }

        [data-testid="stMain"] [data-testid="stRadio"] label p,
        [data-testid="stMain"] [data-testid="stCheckbox"] label p {
            color: #263b31 !important;
            opacity: 1 !important;
        }

        .footnote {
            color: #758278;
            font-size: .78rem;
            border-top: 1px solid #e2e8e0;
            padding-top: 12px;
            margin-top: 26px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center; padding:12px 0;">
            <div style="font-size:3rem;">🌿</div>
            <h1 style="margin:0; color:#ffffff;">VITA</h1>
            <p style="font-size:0.8rem; letter-spacing:1px;">
                INTELLIGENT NUTRITION SYSTEM
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    page = st.radio(
        "NAVIGATION",
        [
            "Home",
            "Nutrition Analyzer",
            "Meal Planner",
            "Food Database",
        ],
        label_visibility="visible",
    )

    st.markdown("---")

    st.caption("Eat well. Feel good. Live better.")


def metric_card(label: str, value: str, unit: str = "") -> None:

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">
                {value}
                <span class="metric-unit">{unit}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,

    )


def meal_card(meal: dict) -> None:
    veg = "Vegetarian" if meal["vegetarian"] else "Non-vegetarian"

    st.markdown(
        f"""
        <div class="meal-card">
            <div class="meal-type">
                {meal['category'].title()} · {veg}
            </div>
            <div class="meal-name">
                {meal['name']}
            </div>
            <div class="meal-meta">
                {meal['calories']} kcal
                &nbsp;·&nbsp;
                Protein {meal['protein']} g
                &nbsp;·&nbsp;
                ₹{meal['cost']} estimated
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


if page == "Home":

    st.markdown(
    """
    <div class="hero">
        <div class="hero-label">YOUR EVERYDAY FOOD COMPANION</div>
        <h1>Eat well. Feel good.</h1>
        <p>
            Understand what's on your plate and plan meals
            that fit your routine and budget.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
    foods_count = len(FOOD_NUTRITION)
    meals_count = len(MEALS)

    a, b, c = st.columns(3)

    with a:
        metric_card(
            "FOODS IN CALCULATOR",
            str(foods_count),
            "items",
        )

    with b:
        metric_card(
            "MEAL IDEAS",
            str(meals_count),
            "options",
        )

    with c:
        metric_card(
            "PLANNING OPTIONS",
            "1 or 7",
            "days",
        )

    st.markdown(
        '<div class="section-title">What would you like to do?</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<p class="muted">Choose a tool from the sidebar to get started.</p>',
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            """
            <div class="meal-card">
                <div class="meal-name">
                    🥑 Nutrition Analyzer
                </div>
                <div class="meal-meta">
                    Estimate calories, protein, carbohydrates
                    and fat for a food portion.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
            <div class="meal-card">
                <div class="meal-name">
                    🍱 Meal Planner
                </div>
                <div class="meal-meta">
                    Build a one-day or seven-day meal plan
                    around your budget and preferences.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.info(
        "Nutrition values and meal costs are estimates. "
        "This tool is for general learning, not medical advice."
    )




elif page == "Nutrition Analyzer":

    st.markdown(
        """
        <div class="section-title">Nutrition Analyzer</div>
        <p class="muted">
            Choose a food and enter the portion size to estimate
            its nutritional values.
        </p>
        """,
        unsafe_allow_html=True,
    )

    with st.form("nutrition_form"):

        left, right = st.columns(2)

        with left:
            food = st.selectbox(
                "Select food",
                sorted(FOOD_NUTRITION.keys()),
                format_func=lambda x: x.title(),
            )

        with right:
            grams = st.number_input(
                "Portion size (grams)",
                min_value=1,
                max_value=5000,
                value=100,
                step=25,
            )

        submitted = st.form_submit_button(
            "Calculate nutrition",
            type="primary",
            use_container_width=True,
        )

    if submitted:

        try:
            result = calculate_nutrition(food, grams)

            st.markdown(
                '<div class="section-title">Your nutrition estimate</div>',
                unsafe_allow_html=True,
            )

            m1, m2, m3, m4 = st.columns(4)

            with m1:
                metric_card(
                    "CALORIES",
                    f"{result['calories']:.1f}",
                    "kcal",
                )

            with m2:
                metric_card(
                    "PROTEIN",
                    f"{result['protein']:.1f}",
                    "g",
                )

            with m3:
                metric_card(
                    "CARBOHYDRATES",
                    f"{result['carbs']:.1f}",
                    "g",
                )

            with m4:
                metric_card(
                    "FAT",
                    f"{result['fat']:.1f}",
                    "g",
                )

            st.caption(
                f"Estimate for {grams:g} g of {food}. "
                "Food values are approximate and may vary by "
                "variety, brand, and preparation."
            )

        except ValueError as exc:
            st.error(str(exc))

    with st.expander("View all supported foods"):

        st.write(
            ", ".join(
                name.title()
                for name in sorted(FOOD_NUTRITION)
            )
        )



elif page == "Meal Planner":

    st.markdown(
        """
        <div class="section-title">Meal Planner</div>
        <p class="muted">
            Create a personalized meal plan using VITA's
            built-in food and meal database.
        </p>
        """,
        unsafe_allow_html=True,
    )

    with st.form("meal_preferences"):

        col1, col2 = st.columns(2)

        with col1:

            duration = st.radio(
                "Plan duration",
                ["One day", "Seven days"],
                horizontal=True,
            )

            diet = st.selectbox(
                "Food preference",
                [
                    "Vegetarian only",
                    "Include non-vegetarian meals",
                ],
            )

            goal_label = st.selectbox(
                "Main goal",
                [
                    "Balanced meals",
                    "High protein",
                    "Budget friendly",
                ],
            )

        with col2:

            budget = st.number_input(
                "Daily food budget (₹)",
                min_value=1,
                max_value=10000,
                value=200,
                step=25,
            )

            hostel = st.checkbox(
                "Only no-cook, kettle or microwave-friendly meals"
            )

            avoid_text = st.text_input(
                "Foods to avoid (comma-separated)",
                placeholder="e.g. peanuts, milk",
            )

        generate = st.form_submit_button(
            "Generate meal plan",
            type="primary",
            use_container_width=True,
        )

    if generate:

        preferences = {
            "vegetarian": diet == "Vegetarian only",
            "budget": float(budget),
            "hostel": hostel,
            "allergies": [
                x.strip().lower()
                for x in avoid_text.split(",")
                if x.strip()
            ],
            "goal": {
                "Balanced meals": "balanced",
                "High protein": "high-protein",
                "Budget friendly": "budget",
            }[goal_label],
        }

        available = {
            cat: filter_meals(cat, preferences)
            for cat in CATEGORIES
        }

        missing = [
            cat
            for cat, options in available.items()
            if not options
        ]

        if missing:

            st.error(
                "No meals matched your choices for: "
                + ", ".join(missing)
                + ". Try changing the food preference, "
                "hostel setting, or foods to avoid."
            )

        else:

            days = 1 if duration == "One day" else 7

            plans = []

            for _ in range(days):

              
                day_preferences = dict(preferences)

                meals = choose_daily_meals(day_preferences)

                if meals is None:
                    meals = [
                        random.choice(available[cat])
                        for cat in CATEGORIES
                    ]

                plans.append(meals)

            totals_week = {
                "calories": 0,
                "protein": 0,
                "carbs": 0,
                "fat": 0,
                "cost": 0,
            }

            for idx, meals in enumerate(plans, start=1):

                if days == 7:
                    st.markdown(
                        f'<div class="section-title">Day {idx}</div>',
                        unsafe_allow_html=True,
                    )

                total = {
                    key: sum(meal[key] for meal in meals)
                    for key in totals_week
                }

                for key in totals_week:
                    totals_week[key] += total[key]

                cols = st.columns(2)

                for i, meal in enumerate(meals):

                    with cols[i % 2]:
                        meal_card(meal)

                st.caption(
                    f"Daily estimate: {total['calories']} kcal"
                    f" · Protein {total['protein']} g"
                    f" · Carbs {total['carbs']} g"
                    f" · Fat {total['fat']} g"
                    f" · Cost ₹{total['cost']}"
                )

                if total["cost"] > budget:

                    st.warning(
                        f"Day {idx} is estimated at ₹{total['cost']}, "
                        f"above your ₹{budget} budget. "
                        "Try a larger budget or choose budget-friendly meals."
                    )

            st.markdown(
                '<div class="section-title">Plan summary</div>',
                unsafe_allow_html=True,
            )

            x1, x2, x3 = st.columns(3)

            with x1:
                metric_card(
                    "TOTAL ESTIMATED COST",
                    f"₹{totals_week['cost']}",
                    f"for {days} day(s)",
                )

            with x2:
                metric_card(
                    "AVERAGE DAILY COST",
                    f"₹{totals_week['cost'] / days:.0f}",
                    "per day",
                )

            with x3:
                metric_card(
                    "TOTAL CALORIES",
                    f"{totals_week['calories']}",
                    "kcal",
                )

            st.caption(
                "Check ingredient labels carefully if you have "
                "an allergy. Meal prices and nutrition are estimates."
            )





elif page == "Food Database":

    st.markdown(
        """
        <div class="section-title">Food Database</div>
        <p class="muted">
            Explore approximate nutritional values per 100 grams.
        </p>
        """,
        unsafe_allow_html=True,
    )

    search = st.text_input(
        "Search food",
        placeholder="Type a food name...",
    )

    rows = []

    for name, values in sorted(FOOD_NUTRITION.items()):

        if search.strip().lower() in name.lower():

            rows.append(
                {
                    "Food": name.title(),
                    "Calories (kcal)": values["calories"],
                    "Protein (g)": values["protein"],
                    "Carbs (g)": values["carbs"],
                    "Fat (g)": values["fat"],
                }
            )

    if rows:

        st.dataframe(
            rows,
            use_container_width=True,
            hide_index=True,
        )

    else:

        st.warning("No foods matched that search.")




st.markdown(
    """
    <div class="footnote">
        🌿 VITA · Intelligent Nutrition System
        &nbsp; | &nbsp;
        Eat Well. Live Well.
        &nbsp; | &nbsp;
        Estimates are illustrative and not medical advice.
    </div>
    """,
    unsafe_allow_html=True,
)