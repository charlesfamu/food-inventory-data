# generate_mock_data.py

import random
import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# Predefined lists of realistic items for each category
pantry_data = {
    "Grains": ["Rice", "Pasta", "Quinoa", "Oats", "Couscous", "Barley", "Bread", "Flour"],
    "Canned Goods": ["Tomato Sauce", "Canned Tuna", "Canned Beans", "Canned Corn", "Soup", "Tomato Paste", "Canned Fruit", "Canned Vegetables"],
    "Baking": ["Flour", "White Sugar", "Baking Powder", "Yeast", "Cocoa Powder", "Chocolate Chips", "Vanilla Extract", "Baking Soda"],
    "Snacks": ["Chips", "Cookies", "Crackers", "Popcorn", "Granola Bars", "Pretzels", "Nuts", "Trail Mix"]
}

fridge_data = {
    "Dairy": ["Milk", "Cheddar Cheese", "Yogurt", "Butter", "Cream", "Eggs", "Sour Cream", "Mozzarella Cheese", "Parmesan Cheese"],
    "Meat": ["Chicken Breast", "Ground Beef", "Pork Chops", "Bacon", "Turkey", "Italian Sausage", "Salmon", "Chicken Thighs", "Shrimp", "Lamb"],
    "Vegetables": ["Carrots", "Lettuce", "Bell Peppers", "Cucumbers", "Broccoli", "Spinach", "Tomatoes", "Zucchini", "Green Beans", "Mushrooms"],
    "Fruits": ["Apples", "Grapes", "Oranges", "Strawberries", "Blueberries", "Bananas", "Pineapple", "Watermelon", "Cantaloupe", "Kiwi", "Mango"],
    "Condiments": ["Ketchup", "Mustard", "Mayonnaise", "Salad Dressing", "Soy Sauce", "Hot Sauce", "BBQ Sauce", "Worcestershire Sauce"],
}

spices = [
    "Cumin", 
    "Paprika", 
    "Oregano", 
    "Basil", 
    "Cinnamon", 
    "Turmeric", 
    "Black Pepper", 
    "Chili Powder", 
    "Garlic Powder", 
    "Ginger", 
    "Thyme", 
    "Italian Seasoning",
    "Salt",
    "Onion Powder",
    "Rosemary",
    "Coriander",
    "Red Pepper Flakes",
    "Bay Leaves",
    "Nutmeg",
    "Cardamom"
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
fridge_df = generate_fridge_data(20)
spice_df = generate_spice_data(10)

# Save to CSV
pantry_df.to_csv('../data/pantry_mock_data.csv', index=False)
fridge_df.to_csv('../data/fridge_mock_data.csv', index=False)
spice_df.to_csv('../data/spice_mock_data.csv', index=False)

print("Mock data generated and saved to CSV.")
