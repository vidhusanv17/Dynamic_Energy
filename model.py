import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load historical energy data
data = pd.read_csv('energy.csv')

# Define features (X) and target variable (y)
X = data[['panel_id', 'energy_input']]
y = data['energy_output']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on test set
y_pred = model.predict(X_test)

# Plot predicted power output per panel
plt.scatter(X_test['panel_id'], y_test, label='Actual')
plt.scatter(X_test['panel_id'], y_pred, label='Predicted')
plt.xlabel('Panel ID')
plt.ylabel('Power Output (W)')
plt.title('Predicted Power Output per Panel')
plt.legend()
plt.show()