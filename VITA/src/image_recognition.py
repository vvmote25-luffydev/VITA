"""Optional pretrained AI food-image classifier.

This feature is separate from the core nutrition calculator and meal planner.
It predicts image labels; it cannot determine portion size or exact nutrition.
Install optional dependencies from requirements-ai.txt before using it.
"""


def recognize_food_image():
    image_path = input("Enter the full path to a food image: ").strip().strip('"')
    if not image_path:
        print("No image path entered.")
        return

    try:
        from PIL import Image
        from transformers import pipeline
    except ImportError:
        print("Optional AI packages are missing.")
        print("Run: python -m pip install -r requirements-ai.txt")
        return

    try:
        with Image.open(image_path) as opened_image:
            image = opened_image.convert("RGB")
    except (OSError, ValueError) as error:
        print(f"Could not open the image. Check the path and file type. ({error})")
        return

    print("\nLoading the food image model. The first run may download model files...")
    try:
        classifier = pipeline("image-classification", model="nateraw/food")
        predictions = classifier(image, top_k=5)
    except Exception as error:
        print("The model could not run. Check your internet connection and installed packages.")
        print(f"Details: {error}")
        return

    print("\nAI food-image predictions:")
    for prediction in predictions:
        label = prediction.get("label", "Unknown")
        confidence = float(prediction.get("score", 0.0)) * 100
        print(f"- {label}: {confidence:.1f}% confidence")
    print("\nPredictions may be incorrect. A photo alone cannot reliably determine serving size or nutrition.")
