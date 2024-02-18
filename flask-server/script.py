import pandas as pd

# Load the CSV data into a DataFrame
df = pd.read_csv('cleaned_credit_cards_data.csv')

# Define user preferences and their weights
user_preferences = {'Travel': 0.6, 'Dining': 0.4}

# Calculate weighted features for each credit card
df['Weighted_Feature'] = (
    user_preferences['Travel'] * df['Travel (%)'] +
    user_preferences['Dining'] * df['Dining (%)']
)

# Normalize weighted features
df['Weighted_Feature'] /= sum(user_preferences.values())

# Sort the DataFrame by the weighted feature in descending order
df = df.sort_values(by=['Weighted_Feature', 'Rating'], ascending=False)

# Display the top recommendations
print(df[['Issuer', 'Card', 'Weighted_Feature','Rating']].head(10))