import streamlit as st
from typing import List, Dict, Any
import sys
import os

# Add the src directory to the path so we can import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import models 
from models.meal import Recipe, Ingredient, MealPlan, UserPreferences

# Set page configuration
st.set_page_config(
    page_title="AI Meal Planner",
    page_icon="🍲",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Sidebar for navigation
    st.sidebar.title("AI Meal Planner")
    page = st.sidebar.radio(
        "Select a page",
        ["Home", "Meal Planner", "Grocery List", "Recipes", "Settings"]
    )
    
    # Page content
    if page == "Home":
        home_page()
    elif page == "Meal Planner":
        meal_planner_page()
    elif page == "Grocery List":
        grocery_list_page()
    elif page == "Recipes":
        recipes_page()
    elif page == "Settings":
        settings_page()

def home_page():
    st.title("🍲 AI-Powered Meal Planning System")
    
    st.markdown("""
    Welcome to your intelligent meal planning assistant! This application helps you:
    
    - Create personalized meal plans based on your preferences
    - Generate smart grocery lists organized by store sections
    - Discover new recipes that match your taste
    - Optimize your food budget
    
    Get started by navigating to the Meal Planner section or customize your preferences in Settings.
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("### 📝 Plan Meals")
        st.markdown("Create a personalized meal plan based on your preferences, dietary restrictions, and available time.")
        st.button("Create Meal Plan", key="home_plan", on_click=meal_planner_page)
    
    with col2:
        st.success("### 🛒 Shop Efficiently")
        st.markdown("Get an organized grocery list categorized by store sections to make shopping quick and easy.")
        st.button("Generate Grocery List", key="home_grocery", on_click=grocery_list_page)
    
    with col3:
        st.warning("### 🍳 Discover Recipes")
        st.markdown("Find new recipes that match your preferences or use ingredients you already have.")
        st.button("Find Recipes", key="home_recipes", on_click=recipes_page)

def meal_planner_page():
    st.title("Meal Planner")
    
    # Meal Planning form
    with st.form("meal_plan_form"):
        st.subheader("Create a new meal plan")
        
        # Days selector
        days = st.slider("Number of days", 1, 14, 7)
        
        # Meal types
        meal_types = st.multiselect(
            "Meals to include",
            ["Breakfast", "Lunch", "Dinner", "Snacks"],
            default=["Breakfast", "Lunch", "Dinner"]
        )
        
        # Dietary restrictions
        dietary_restrictions = st.multiselect(
            "Dietary restrictions",
            ["Vegetarian", "Vegan", "Gluten-Free", "Dairy-Free", "Keto", "Paleo"],
            default=[]
        )
        
        # Cuisine preferences
        cuisines = st.multiselect(
            "Preferred cuisines",
            ["Italian", "Mexican", "Asian", "Mediterranean", "American", "Indian", "French"],
            default=[]
        )
        
        # Budget
        budget = st.select_slider(
            "Budget level",
            options=["Economy", "Moderate", "Premium"],
            value="Moderate"
        )
        
        # Submit button
        submitted = st.form_submit_button("Generate Meal Plan")
        
        if submitted:
            st.info("Generating your personalized meal plan...")
            # Here we would call the backend service
            # For the MVP, we'll just display a placeholder
            st.success("Meal plan generated successfully!")
            
            # Display a sample meal plan
            st.subheader("Your 7-Day Meal Plan")
            sample_plan = {
                "Monday": {"Breakfast": "Avocado Toast", "Lunch": "Chicken Salad", "Dinner": "Pasta Primavera"},
                "Tuesday": {"Breakfast": "Smoothie Bowl", "Lunch": "Veggie Wrap", "Dinner": "Salmon with Roasted Vegetables"},
                # Add more days as needed
            }
            
            for day, meals in sample_plan.items():
                st.markdown(f"#### {day}")
                for meal_type, meal in meals.items():
                    st.markdown(f"**{meal_type}**: {meal}")
                st.markdown("---")

def grocery_list_page():
    st.title("Grocery List")
    
    # Display a sample grocery list
    st.info("Based on your current meal plan, here's your optimized grocery list:")
    
    # Sample grocery list by category
    grocery_categories = {
        "Produce": ["Spinach (2 bunches)", "Tomatoes (4)", "Avocados (2)", "Onions (3)", "Garlic (1 head)"],
        "Meat & Seafood": ["Chicken breast (1 lb)", "Ground turkey (1 lb)", "Salmon fillets (2)"],
        "Dairy & Eggs": ["Eggs (1 dozen)", "Greek yogurt (32 oz)", "Cheddar cheese (8 oz)"],
        "Pantry": ["Pasta (1 box)", "Rice (1 lb)", "Olive oil", "Canned black beans (2 cans)"],
        "Bakery": ["Whole grain bread (1 loaf)"]
    }
    
    for category, items in grocery_categories.items():
        with st.expander(f"{category} ({len(items)} items)"):
            for item in items:
                st.checkbox(item)
    
    col1, col2 = st.columns(2)
    with col1:
        st.download_button("Download Grocery List", "Sample grocery list content", "grocery_list.txt")
    with col2:
        st.button("Email Grocery List")

def recipes_page():
    st.title("Recipe Finder")
    
    search_term = st.text_input("Search for recipes")
    
    # Filters
    col1, col2 = st.columns(2)
    with col1:
        diet = st.multiselect(
            "Dietary Restrictions",
            ["Vegetarian", "Vegan", "Gluten-Free", "Dairy-Free"]
        )
    with col2:
        cuisine = st.multiselect(
            "Cuisine Type",
            ["Italian", "Mexican", "Asian", "Mediterranean", "American"]
        )
    
    if search_term:
        st.success(f"Showing results for '{search_term}'")
        
        # Display sample recipes
        for i in range(3):
            st.markdown(f"### Sample Recipe {i+1}")
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image("https://via.placeholder.com/150", caption=f"Recipe {i+1}")
            with col2:
                st.markdown(f"**Description**: A delicious recipe that matches your search for '{search_term}'")
                st.markdown("**Ingredients**: Ingredient 1, Ingredient 2, Ingredient 3")
                st.markdown("**Time to make**: 30 minutes")
                st.button("Add to Meal Plan", key=f"add_recipe_{i}")
            
            st.markdown("---")
    else:
        st.info("Enter a search term to find recipes")
        
        # Show recommended recipes
        st.subheader("Recommended for you")
        for i in range(3):
            st.markdown(f"### Recommendation {i+1}")
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image("https://via.placeholder.com/150", caption=f"Recipe {i+1}")
            with col2:
                st.markdown("**Description**: A recipe we think you'll enjoy based on your preferences")
                st.markdown("**Ingredients**: Ingredient 1, Ingredient 2, Ingredient 3")
                st.markdown("**Time to make**: 25 minutes")
                st.button("Add to Meal Plan", key=f"add_rec_{i}")
            
            st.markdown("---")

def settings_page():
    st.title("Settings & Preferences")
    
    st.subheader("User Profile")
    name = st.text_input("Name", "")
    household_size = st.number_input("Household Size", 1, 10, 2)
    
    st.subheader("Dietary Preferences")
    dietary_restrictions = st.multiselect(
        "Dietary Restrictions",
        ["Vegetarian", "Vegan", "Gluten-Free", "Dairy-Free", "Keto", "Paleo"],
        default=[]
    )
    
    allergies = st.multiselect(
        "Allergies",
        ["Nuts", "Shellfish", "Eggs", "Soy", "Wheat", "Dairy"],
        default=[]
    )
    
    st.subheader("Shopping Preferences")
    preferred_stores = st.multiselect(
        "Preferred Grocery Stores",
        ["Any Store", "Whole Foods", "Trader Joe's", "Kroger", "Walmart", "Target"],
        default=["Any Store"]
    )
    
    budget_preference = st.select_slider(
        "Budget Level",
        options=["Economy", "Moderate", "Premium"],
        value="Moderate"
    )
    
    st.subheader("Recipe Preferences")
    max_cooking_time = st.slider("Maximum Cooking Time (minutes)", 15, 120, 45)
    cuisine_preferences = st.multiselect(
        "Preferred Cuisines",
        ["Italian", "Mexican", "Asian", "Mediterranean", "American", "Indian", "French"],
        default=[]
    )
    
    if st.button("Save Preferences"):
        st.success("Preferences saved successfully!")

if __name__ == "__main__":
    main() 