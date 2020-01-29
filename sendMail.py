"""
This call sends a message to the given recipient with vars and custom vars.
"""
from mailjet_rest import Client
import os

api_key = os.environ['xxx'] api_secret = os.environ['XXX'] mailjet = Client(auth=(api_key, api_secret), version='v3.1') data = {
   'Messages': [
         {
             "From": {
                 "Email": "mirko.muller@he-arc.ch",
                 "Name": "mirko "
             },
             "To": [
                 {
                     "Email": "passenger1@example.com",
                     "Name": "passenger 1"
                 }
             ],
             "TemplateID": 1013102,
             "TemplateLanguage": True,
             "Subject": "paypal",
             "Variables": {}
         }
     ]
}
result = mailjet.send.create(data=data)
print result.status_code
print result.json()

