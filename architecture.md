# Meal Planning System Architecture

## System Overview - MVP with Streamlit
The meal planning system is designed as an MVP using Streamlit for the frontend. It helps users create personalized meal plans, manage groceries efficiently, and discover new recipes. The system leverages Neo4j for recipe relationships and recommendations, while maintaining a modular architecture that can be easily expanded in the future.

## Core Components

### 1. Data Models (`src/models/`)
- **Recipe**: Core recipe information including ingredients, instructions, and metadata
- **Ingredient**: Detailed ingredient information with categorization
- **MealPlan**: Represents a complete meal plan with dates and preferences
- **UserPreferences**: Stores user-specific settings and dietary requirements

### 2. Database Layer
#### Neo4j Graph Database (`src/database/`)
- Stores recipe relationships and connections
- Manages ingredient substitutions
- Tracks user ratings and preferences
- Enables sophisticated recipe recommendations

Key Relationships:
- Recipe → Ingredient (REQUIRES)
- User → Recipe (RATED)
- Recipe → Recipe (SIMILAR_TO)
- Ingredient → Ingredient (SUBSTITUTES)

### 3. Services (`src/services/`)

#### MealPlannerService
- Generates personalized meal plans
- Optimizes grocery lists
- Finds similar recipes
- Suggests ingredient substitutions

#### RecipeCrawlerService
- Fetches recipes from external sources
- Enriches recipe data with additional information

#### InventoryManager
- Tracks pantry inventory
- Suggests recipes based on available ingredients

#### BudgetOptimizer
- Optimizes meal plans for cost
- Compares prices across stores

### 4. Streamlit Frontend (`src/app.py` and `src/pages/`)
- Provides user interface for interacting with the meal planning system
- Organizes functionality across different pages:
  - Meal Planner
  - Grocery List
  - Recipe Finder
  - Settings & Preferences
- Directly interfaces with backend services

## Data Flow for MVP

1. User Input → Streamlit UI
2. Streamlit → Backend Services
3. Services ↔ Neo4j Database
4. Services → Data Processing
5. Streamlit → User Display

## Technical Stack - MVP

- **Frontend**: Streamlit
- **Backend**: Python functions
- **Database**: Neo4j
- **Data Processing**: Pandas
- **Type Checking**: Python type hints

## Migration Path for Future Growth

The MVP design allows for easy migration to a more scalable architecture:

1. **Separate Frontend**: Replace Streamlit with React/Vue/Angular
2. **API Layer**: Add FastAPI for RESTful endpoints
3. **Containerization**: Add Docker for easy deployment
4. **Authentication**: Implement proper auth system
5. **Caching**: Add Redis for performance

## Future Extensibility

The architecture is designed to easily accommodate:
- Additional data sources
- New recommendation algorithms
- Integration with smart home devices
- Mobile app integration
- Machine learning components

## Performance Considerations for MVP

- Optimized Neo4j queries
- Caching frequently accessed data
- Asynchronous processing where appropriate
- Pagination for large result sets

## Security Considerations

- API authentication and authorization
- Data encryption
- Rate limiting
- Input validation
- Secure storage of user preferences

## Performance Optimization

- Neo4j query optimization
- Caching layer for frequent requests
- Asynchronous processing
- Batch operations for grocery lists 