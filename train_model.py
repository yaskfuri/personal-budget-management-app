import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle

# Load dataset
df = pd.read_csv("transactions.csv")

# Split data into features and target
X = df['description']
y = df['category']

# Create a pipeline: Vectorize text and apply Naive Bayes classifier
model_pipeline = Pipeline([
    ('vectorizer', CountVectorizer()), 
    ('classifier', MultinomialNB())
])

# Train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model_pipeline.fit(X_train, y_train)

# Save the trained model
with open("expense_classifier.pkl", "wb") as f:
    pickle.dump(model_pipeline, f)

print("Model trained and saved!")
