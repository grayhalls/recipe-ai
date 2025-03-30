// Recipe Node
CREATE (r:Recipe {
    id: String,
    name: String,
    prep_time: Integer,
    cook_time: Integer,
    difficulty: String,
    rating: Float
});

// Ingredient Node
CREATE (i:Ingredient {
    id: String,
    name: String,
    category: String
});

// User Node
CREATE (u:User {
    id: String,
    name: String
});

// Relationships
CREATE (r)-[:REQUIRES]->(i);
CREATE (u)-[:RATED {rating: Float}]->(r);
CREATE (r)-[:SIMILAR_TO {score: Float}]->(r);
CREATE (i)-[:SUBSTITUTES]->(i); 