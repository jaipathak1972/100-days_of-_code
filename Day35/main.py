import requests

api = "https://api.openweathermap.org/data/3.0/onecall"
key ="97be2d6f693db91b559b84367a12e593"
weather_parameters = {

    "lat" : 78.962883,
    "lon" : 20.593683,
    "appid" : key    

                        }
reponse = requests.get(api , params= weather_parameters)
print(reponse.json)





