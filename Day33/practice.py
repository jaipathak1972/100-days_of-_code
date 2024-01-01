import requests
from datetime import datetime
response =requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

long = float(data['iss_position']['longitude'])
lati = float(data['iss_position']['latitude'])
parametters ={

    "lat": long,
    "lng": lati,
    "formatted" : 0
}
reponse = requests.get("https://api.sunrise-sunset.org/json" , params= parametters)
data = reponse.json()
sunrise =str(data["results"]["sunrise"]).split("T")[1].split(":")[0]
sunset =str(data["results"]["sunset"]).split("T")[1].split(":")[0]
now_hour = int(datetime.now().hour)
if int(sunrise) < int(now_hour)  < int(sunset):
    print("its day time wake up ")


 
