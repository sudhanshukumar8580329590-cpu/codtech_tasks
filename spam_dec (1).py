from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd

# Example dataset: spam detection
# Each email is labeled as 1 (spam) or 0 (not spam)
data = {
    'text': [
        'Buy 1 get 1 free offer',
        'Win a free iPhone now',
        'Exclusive deal for you',
        'Hey, are we still meeting today?',
        'Lowest prices on car insurance',
        'Call your mom when you get home',
        'Congratulations, you have won a lottery',
        'Can we schedule a meeting for tomorrow?',
        'Limited time offer!!!',
        'Please find attached the project report',
        'Urgent! Your account has been compromised'
    ],
    'label': [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}

# Create DataFrame
df = pd.DataFrame(data)

# Split data
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.3, random_state=42)

# Convert text to numerical vectors
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train a Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Predictions
y_pred = model.predict(X_test_vec)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=False)

accuracy, report
print("Accuracy:", accuracy)
print("\nClassification Report:\n", report)