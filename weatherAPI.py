import requests
import json
city_name = 'San Fracisco'
state_code = 'CA'
country_code = 'US'
API_key = '72cded2ce0c7e35a219f7832836475d9'
response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}')
response.raise_for_status()
geo_data = json.loads(response.text)
lat = geo_data[0]['lat']
lon = geo_data[0]['lon']
print(f"Coordonnées de {city_name} trouvées : Lat {lat}, Lon {lon}")