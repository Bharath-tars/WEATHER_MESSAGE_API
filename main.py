import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = 'your_key'
account_sid = 'your_id'
auth_token = 'your_key'

weather_params = {
    "lat": "17.385044",
    "lon": "78.486671",
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
data = weather_data['weather'][0]['id']
if int(data) < 700:
    content = 'Get an umbrella today.. czee its gonna rain'
else:
    content = 'Its a sunny day.. no need for an umbrella'
client = Client(account_sid, auth_token)
message = client.messages\
    .create(
        body=" hey there☔️",
        from_="ur_no",
        to="to_no"
    )
print(message.status)
