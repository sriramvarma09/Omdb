import json
import pandas as pd
import requests as r


mvinput = input("Enter movie name : ")
mvurl = "http://www.omdbapi.com/?apikey=[APIKEY]&t="+mvinput
fetch = r.get(mvurl)
jsonf = json.loads(fetch.text)
bxoff = jsonf['BoxOffice']
bxoff = (bxoff.lstrip('$')).replace(",", "")
print("Box Office collections in USD : {}".format(bxoff))
convurl = "https://api.getgeoapi.com/v2/currency/convert?api_key=[APIKEY]&from=USD&to=INR&format=json&amount="+bxoff
jsonc = (r.get(convurl)).json()
rupees = jsonc["rates"]['INR']['rate_for_amount']
print("Box Office collections in INR : {}".format(rupees))
