import requests
import json

url = "http://api.fixer.io/latest?base=USD"

response = requests.get(url)

data = response.text

parsed = json.loads(data)


date = parsed["date"]

#gbp_rate = parsed["rates"]["GBP"]
#usd_rate = parsed["rates"]["USD"]
#print("On " + date + " EUR equals " + str(gbp_rate) + " GBP")
#print("On " + date + " EUR equals " + str(usd_rate) + " USD")

print(parsed["rates"])