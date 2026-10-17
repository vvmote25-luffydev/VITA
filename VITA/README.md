# VITA — Food & Nutrition Planner

VITA is a Python food nutrition calculator and rule-based meal planner with a web interface built using Streamlit.

## Features

- Web UI with Home, Nutrition Analyzer, Meal Planner, and Food Database pages.
- Estimate calories, protein, carbohydrates, and fat for supported foods and portion sizes.
- Generate one-day or seven-day meal plans.
- Filter meal suggestions by vegetarian preference, estimated daily budget, hostel-friendly preparation, foods to avoid, and goal.
- Keep a simple terminal interface available through `main.py`.
- Optional AI image classification code is provided separately, but is not required for the web interface.

## Requirements

- Python 3.10 or newer recommended.
- Internet access is needed to install Streamlit. The app's own food data and calculations run locally after installation.

## Run the web interface (recommended)

Open PowerShell in the folder containing `streamlit_app.py`, then run:

```powershell
python -m pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```

Streamlit will print a local address, usually `http://localhost:8501`, and open the app in your browser. If it does not open automatically, copy the local address into your browser.

## Run the terminal interface

```powershell
python main.py
```

## Optional AI image recognition

The separate optional image-recognition feature uses a pretrained model and requires packages listed in `requirements-ai.txt`. It has not been integrated into the Streamlit pages. A model prediction may be incorrect and cannot determine portion size or exact nutrition from an image.

## Project structure

```text
Euron_Food_Nutrition_Planner/
├── main.py
├── streamlit_app.py
├── requirements.txt
├── requirements-ai.txt
├── README.md
├── .gitignore
└── src/
    ├── __init__.py
    ├── app.py
    ├── analyzer.py
    ├── image_recognition.py
    ├── meal_planner.py
    └── nutrition.py
```

## Notes and limitations

- Nutrition data is approximate per 100 g and depends on preparation, recipe, and brand.
- Meal nutrition and prices are illustrative estimates, not guarantees.
- Meal planning uses predefined data and rule-based filtering; it is not an AI recommendation model.
- Check ingredient labels carefully if you have an allergy. This app is for general information and learning, not medical advice.
