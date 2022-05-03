from os import getenv
import requests
import json



def sms_send(phone,text):

    SMS_URI = 'https://api.smsdev.com.br/v1/send'

    data={
    "key" : getenv("SMS_URI_KEY"),
    "type" : 9,
    "number" : phone,
    "msg" : text
    }
    req = requests.post(SMS_URI, data=data)
    