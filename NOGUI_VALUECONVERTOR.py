import requests 
import json
#
resJSON=(requests.get('https://www.cbr-xml-daily.ru/daily_json.js'))
res = json.loads(resJSON.text)
# WHY NO RUB ON RUSSIAN BANK SITE?
values= input("Enter the values for matching: \"VALUE1\" SPACE \"VALUE2\" \n")
val1, val2 = '', ''
val1 = values[0:3]
val2 = values[4:7]
VALUEdICT1 = res["Valute"][val1]
VALUEdICT2 = res["Valute"][val2]
print(f"1 {val1} = {res["Valute"][val1]['Value']/res["Valute"][val2]["Value"]} {val2}\n")
input("PRESS ENTER TO QUIT...")