import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load the dataset

data = pd.read_csv("C:\\Users\\Dipansh Gupta\\Desktop\\phython\\emoji_data.csv")
# Split the data into text and labels
X = data['text']
y = data['emoji']

# Convert text to numerical features
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Train the Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate the model
from sklearn.metrics import accuracy_score
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Make predictions
new_text = ['great day']
new_text_vectorized = vectorizer.transform(new_text)
predicted_emoji = model.predict(new_text_vectorized)
print(f'Predicted emoji for "{new_text[0]}": {predicted_emoji[0]}')