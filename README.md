# AI-Powered Meal Planning System

An intelligent meal planning system that helps users create personalized meal plans, manage groceries, and discover new recipes using AI and graph-based recommendations.

## Features

- 🗓️ Personalized meal planning
- 🛒 Smart grocery list generation
- 💡 Recipe recommendations
- 💰 Budget optimization
- 🔄 Ingredient substitutions
- 📊 Pantry inventory management

## Getting Started

### Prerequisites

- Python 3.8+
- Neo4j Desktop (for local development)
- Streamlit
- Pip or Poetry (for dependency management)

### Installation

1. Clone the repository
   ```
   git clone https://github.com/grayhalls/recipe-ai.git
   cd recipe-ai
   ```

2. Install dependencies
   ```
   pip install -r requirements.txt
   # Or if using Poetry
   # poetry install
   ```

3. Set up Neo4j
   - Install [Neo4j Desktop](https://neo4j.com/download/)
   - Create a new database with password (save for configuration)
   - Start the database

4. Configure environment variables
   ```
   cp .env.example .env
   # Edit .env with your Neo4j credentials and configuration
   ```

5. Run the Streamlit application
   ```
   streamlit run src/app.py
   ```

## Project Structure

```
recipe-ai/
├── src/
│   ├── app.py                # Main Streamlit application
│   ├── pages/                # Additional Streamlit pages
│   │   ├── meal_planner.py
│   │   ├── grocery_list.py
│   │   └── recipe_finder.py
│   ├── api/                  # Backend functions for Streamlit
│   ├── models/               # Data models
│   ├── services/             # Business logic
│   ├── database/             # Database schemas and connections
│   └── utils/                # Helper functions
├── data/                     # Sample data and schema files
├── tests/                    # Tests
├── requirements.txt          # Dependencies
└── README.md
```

## Streamlit UI

The MVP uses Streamlit for a quick, Python-centric UI. Features include:
- Interactive meal plan creation
- Grocery list generation and categorization
- Recipe recommendations
- Preference management

## To Do Items:
- recipe input processor (using image and url to have an agent generate the Neo4j cypher query)
- personalized per user
   - allow users to select and insert their own recipes and save
- actually want a chatbot on the homepage

## Future Enhancements

- Custom UI with dark gradient background
- Mobile application
- Docker containerization for easier deployment
- Integration with grocery delivery services
- Smart home device integration

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

### Usage

Access the API documentation at `http://localhost:8000/docs`

Example API calls:
