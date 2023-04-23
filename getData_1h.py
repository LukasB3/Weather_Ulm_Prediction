import requests
import pandas as pd
from datetime import datetime, timedelta

API_KEY = '5ee2ba8771a162d5713270004aef3e58'

CITY_NAME = 'Ulm'

url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric'
response = requests.get(url)
data = response.json()

main_data = data['main']
weather_data = data['weather'][0]
wind_data = data['wind']
sys_data = data['sys']
clouds_data = data['clouds']
rain_data = data.get('rain', {})
snow_data = data.get('snow', {})
rain_volume_1h = rain_data.get('1h', 0)
rain_volume_3h = rain_data.get('3h', 0)
snow_volume_1h = snow_data.get('1h', 0)
snow_volume_3h = snow_data.get('3h', 0)

current_utc_datetime = datetime.utcnow()
timezone_offset = timedelta(seconds=data['timezone'])
local_datetime = current_utc_datetime + timezone_offset

weather_dict = {
    'City': CITY_NAME,
    'Latitude': data['coord']['lat'],
    'Longitude': data['coord']['lon'],
    'Temperature': main_data['temp'],
    'Temp_min': main_data['temp_min'],
    'Temp_max': main_data['temp_max'],
    'Feels_like': main_data['feels_like'],
    'Pressure': main_data['pressure'],
    'Humidity': main_data['humidity'],
    'Dew_Point': main_data.get('dew_point', None),
    'Wind_Speed': wind_data['speed'],
    'Wind_Direction': wind_data.get('deg', None),
    'Wind_Gust': wind_data.get('gust', None),
    'Cloudiness': clouds_data['all'],
    'Rain_Volume_1h': rain_volume_1h,
    'Rain_Volume_3h': rain_volume_3h,
    'Snow_Volume_1h': snow_volume_1h,
    'Snow_Volume_3h': snow_volume_3h,
    'Weather_Id': weather_data['id'],
    'Weather': weather_data['main'],
    'Description': weather_data['description'],
    'Weather_Icon': weather_data['icon'],
    'Visibility': data.get('visibility', None),
    'Date_Time': local_datetime,
    'Timezone': data['timezone'],
    'Sunrise': pd.to_datetime(sys_data['sunrise'], unit='s'),
    'Sunset': pd.to_datetime(sys_data['sunset'], unit='s'),
}

weather_df = pd.DataFrame(weather_dict, index=[0])
