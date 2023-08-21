import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import datetime

# Load the dataset
data = pd.read_csv("spy-prices.csv")
data['Date'] = pd.to_datetime(data['Date'])
data['Timestamp'] = data['Date'].apply(lambda x: (x - datetime.datetime(1970, 1, 1, tzinfo=None)).total_seconds())

# Preprocess data
X = data[['Timestamp']]
y = data['Close']  # You can also use 'Adj Close' depending on your needs

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize model
model = LinearRegression()

# Cross-validation
cv_scores = cross_val_score(model, X_train, y_train, cv=5)
print("CV Scores:", cv_scores)

# Train the model
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

def predict_future_price(timestamp: str) -> float:
    """
    Predict the future price given a timestamp.
    """
    date_obj = datetime.datetime.strptime(timestamp, "%Y-%m-%d")
    future_timestamp = [[(date_obj - datetime.datetime(1970, 1, 1)).total_seconds()]]  # Ensure it's 2D
    return model.predict(future_timestamp)[0]

if __name__ == "__main__":
    # Test the prediction
    timestamp = "2025-01-01"
    prediction = predict_future_price(timestamp)
    print(f"Predicted price for {timestamp}: ${prediction:.2f}")
