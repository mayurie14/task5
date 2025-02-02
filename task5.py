import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap

# Sample traffic accident data
data = {
    'Date': pd.date_range(start='2024-01-01', periods=10, freq='D'),
    'Time': ['08:00', '14:30', '19:45', '23:15', '06:20', '12:00', '18:50', '21:30', '15:00', '09:15'],
    'Weather': ['Clear', 'Rain', 'Snow', 'Fog', 'Clear', 'Rain', 'Fog', 'Snow', 'Clear', 'Rain'],
    'Road_Condition': ['Dry', 'Wet', 'Icy', 'Dry', 'Wet', 'Dry', 'Icy', 'Wet', 'Dry', 'Icy'],
    'Severity': [2, 3, 4, 1, 2, 3, 5, 2, 1, 4],
    'Latitude': [37.77, 37.78, 37.79, 37.76, 37.75, 37.77, 37.78, 37.79, 37.76, 37.75],
    'Longitude': [-122.42, -122.43, -122.44, -122.41, -122.40, -122.42, -122.43, -122.44, -122.41, -122.40]
}

df = pd.DataFrame(data)

# Convert Time to datetime for time-based analysis
df['Hour'] = pd.to_datetime(df['Time']).dt.hour

# Accident Severity Distribution
sns.countplot(x='Severity', data=df, palette='coolwarm')
plt.title('Accident Severity Distribution')
plt.show()

# Accidents by Weather Condition
sns.countplot(x='Weather', data=df, palette='Blues')
plt.title('Accidents by Weather Condition')
plt.show()

# Accidents by Road Condition
sns.countplot(x='Road_Condition', data=df, palette='Greens')
plt.title('Accidents by Road Condition')
plt.show()

# Accidents by Time of Day
sns.histplot(df['Hour'], bins=8, kde=True, color='purple')
plt.title('Accidents by Time of Day')
plt.xlabel('Hour of Day')
plt.show()

# Heatmap of Accident Hotspots
m = folium.Map(location=[37.77, -122.42], zoom_start=12)
HeatMap(data=df[['Latitude', 'Longitude']].values, radius=15).add_to(m)

# Save the map to an HTML file
m.save('accident_hotspots.html')

print("Accident hotspot map saved as 'accident_hotspots.html'")
