#get weather data

import requests
import matplotlib.pyplot as plt

city_name = 'bhopal'
API_key='1188e26b3faaa41b2e8b58d6baa2537e'
url= f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

response= requests.get(url)
if response.status_code == 200:
    data=response.json()
    print('Weather of your city is :',data['weather'][0]['description'])
    print('Current temperature is :',data['main']['temp'])
    print('Current temperature feels like : ',data['main']['feels_like'])
    print('Todays minimum temperature is :',data['main']['temp_min'])
    print('Todays maximum temperature is :',data['main']['temp_max'])
    print('Humidity is : ',data['main']['humidity'])
    print('Pressure is :',data['main']['pressure'])
    print('Wind speed is :',data['wind']['speed'])
    
    # Adding matplotlib visualization
    # Plotting temperature data
    temperatures = [data['main']['temp'], data['main']['feels_like'], data['main']['temp_min'], data['main']['temp_max']]
    labels = ['Current', 'Feels Like', 'Min', 'Max']
    
    plt.figure(figsize=(8, 5))
    plt.bar(labels, temperatures, color=['blue', 'orange', 'green', 'red'])
    plt.ylabel('Temperature (°C)')
    plt.title(f'Temperature Data for {city_name}')
    plt.ylim(min(temperatures) - 5, max(temperatures) + 5)  # Adjust y-axis for better view
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    
    # Optional: Plot humidity and pressure as a simple bar chart
    other_data = [data['main']['humidity'], data['main']['pressure']]
    other_labels = ['Humidity (%)', 'Pressure (hPa)']
    
    plt.figure(figsize=(6, 4))
    plt.bar(other_labels, other_data, color=['purple', 'brown'])
    plt.title(f'Humidity and Pressure for {city_name}')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    
else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")
    print(response.text)
