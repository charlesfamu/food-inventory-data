# generate_mock_data.py

import random
import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# Predefined lists of realistic items for each category
pantry_data = {
    "Grains": ["Rice", "Pasta", "Quinoa", "Oats", "Couscous"],
    "Canned Goods": ["Tomato Sauce", "Canned Tuna", "Canned Beans", "Canned Corn", "Soup", "Tomato Paste"],
    "Baking": ["Flour", "Sugar", "Baking Powder", "Yeast", "Cocoa Powder"],
    "Snacks": ["Chips", "Cookies", "Crackers", "Popcorn", "Granola Bars"],
    "Condiments": ["Ketchup", "Mustard", "Mayonnaise", "Soy Sauce", "Hot Sauce"]
}

fridge_data = {
    "Dairy": ["Milk", "Cheese", "Yogurt", "Butter", "Cream"],
    "Meat": ["Chicken Breast", "Ground Beef", "Pork Chops", "Bacon", "Turkey"],
    "Vegetables": ["Carrots", "Lettuce", "Bell Peppers", "Cucumbers", "Broccoli"],
    "Fruits": ["Apples", "Grapes", "Oranges", "Strawberries", "Blueberries"],
    "Condiments": ["Ketchup", "Mustard", "Mayonnaise", "Salad Dressing", "Soy Sauce"]
}

spices = [
    "Cumin", "Paprika", "Oregano", "Basil", "Cinnamon", "Turmeric", "Pepper", "Chili Powder", "Garlic Powder", "Ginger", "Tyhme", "Italian Seasoning"
]

# Function to generate mock data for pantry with correct category-item pairing
def generate_pantry_data(n=10):
    data = []
    for _ in range(n):
        category = random.choice(list(pantry_data.keys()))
        item_name = random.choice(pantry_data[category])
        data.append({
            'Item Name': item_name,
            'Category': category,
            'Quantity': f"{random.randint(1, 10)} {random.choice(['bags', 'cans', 'boxes'])}",
            'Expiry Date': fake.date_between(start_date='today', end_date='+2y'),
            'Purchase Date': fake.date_between(start_date='-2y', end_date='today'),
            'Brand': fake.company(),
        })
    return pd.DataFrame(data)

# Function to generate mock data for fridge with correct type-item pairing
def generate_fridge_data(n=10):
    data = []
    for _ in range(n):
        item_type = random.choice(list(fridge_data.keys()))
        item_name = random.choice(fridge_data[item_type])
        data.append({
            'Item Name': item_name,
            'Type': item_type,
            'Quantity': f"{random.randint(1, 5)} {random.choice(['cartons', 'lbs', 'pieces'])}",
            'Expiry Date': fake.date_between(start_date='today', end_date='+1y'),
            'Storage Location': random.choice(['Top Shelf', 'Bottom Shelf', 'Drawer', 'Door']),
        })
    return pd.DataFrame(data)

# Function to generate mock data for spice drawer
def generate_spice_data(n=10):
    types = ["Ground", "Whole"]
    data = []
    for _ in range(n):
        data.append({
            'Spice Name': random.choice(spices),
            'Quantity': f"{random.randint(50, 500)}g",
            'Expiry Date': fake.date_between(start_date='today', end_date='+3y'),
            'Type': random.choice(types),
        })
    return pd.DataFrame(data)

# Generate mock data
pantry_df = generate_pantry_data(15)
fridge_df = generate_fridge_data(10)
spice_df = generate_spice_data(8)

# Save to CSV
pantry_df.to_csv('data/pantry_mock_data.csv', index=False)
fridge_df.to_csv('data/fridge_mock_data.csv', index=False)
spice_df.to_csv('data/spice_mock_data.csv', index=False)

print("Mock data generated and saved to CSV.")
