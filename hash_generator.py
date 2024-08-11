from datetime import datetime
import json
import hmac
from hashlib import sha512
import urllib.parse

main_url = "www.google.com"
secret = "35479y6q45@#$%^&748974%^&*ypyt8"

##=========================== Get Method ===========================##

#Todays date
todaysdate = datetime.now().isoformat()+'Z'

#URL Encode
get_url_encoded = urllib.parse.quote(main_url, safe='').encode().decode()

#Concate request method and URL
method_url = "GET&"+str(get_url_encoded)

#Generate Signature using All encoded data
computed_sig = hmac.new(secret.encode(),msg=method_url.encode(),digestmod=sha512).hexdigest()




##=========================== POST method =============================##

#Todays date
todaysdate = datetime.now().isoformat()+'Z'

#URL Encode
B_encoded = urllib.parse.quote(main_url,safe='').encode().decode()

#Concate request method and URL
base_string = 'POST&'+B_encoded

#Dictionary data to be sent with Oder create API.
string_data = {"firstname":"firstname","lastname":"lastname","email":"myemail@email.com","mobile":"000000000"}

#Data converted into JSON Format
payload = json.dumps(string_data,sort_keys=True,separators=(',',':'))

#Encoded JSON
encoded_payload = urllib.parse.quote(payload, safe='').encode().decode()

#Concate request method , URL and JSON
final_payload = base_string+'&'+encoded_payload

#Encode Concated data
all_encoded = final_payload.encode()

#Generate Signature using All encoded data
computed_sig = hmac.new(secret.encode(),msg=all_encoded,digestmod=sha512).hexdigest()