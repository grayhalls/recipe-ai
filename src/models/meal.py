from datetime import datetime
from typing import List, Optional

class Recipe:
    def __init__(self):
        self.id: str
        self.name: str
        self.ingredients: List[Ingredient]
        self.instructions: List[str]
        self.prep_time: int
        self.cook_time: int
        self.servings: int
        self.cuisine_type: str
        self.dietary_restrictions: List[str]
        self.source_url: Optional[str]
        self.nutrition_info: NutritionInfo

class Ingredient:
    def __init__(self):
        self.id: str
        self.name: str
        self.category: str  # produce, meat, dairy, pantry, etc.
        self.quantity: float
        self.unit: str
        self.estimated_price: float
        self.store_section: str

class MealPlan:
    def __init__(self):
        self.id: str
        self.start_date: datetime
        self.end_date: datetime
        self.meals: List[PlannedMeal]
        self.user_preferences: UserPreferences
        self.grocery_list: GroceryList

class UserPreferences:
    def __init__(self):
        self.dietary_restrictions: List[str]
        self.cuisine_preferences: List[str]
        self.budget_per_meal: float
        self.preferred_stores: List[str]
        self.cooking_skill_level: str
        self.household_size: int 