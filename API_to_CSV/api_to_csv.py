import pandas as pd
import requests
api_url = 'https://data.binance.com/api/v3/ticker/24hr'  
response = requests.get(api_url)
if response.status_code == 200:
    api_data = response.json()  
else:
    print("Failed to retrieve data from the API")
df = pd.DataFrame(api_data)
df.to_csv('api_data.csv', index=False)
