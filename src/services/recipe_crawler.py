from typing import List

class RecipeCrawlerService:
    def __init__(self, api_clients):
        self.api_clients = api_clients

    async def fetch_new_recipes(self) -> List[Recipe]:
        """Fetch recipes from various sources (APIs, websites)."""
        pass

    async def enrich_recipe_data(self, recipe: Recipe) -> Recipe:
        """Add additional data like nutritional info and images."""
        pass 