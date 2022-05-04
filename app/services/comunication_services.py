from os import getenv
import requests


def sms_send(phone:int,text:str):

    SMS_URI = 'https://api.smsdev.com.br/v1/send'

    data={
        "key" : getenv("SMS_URI_KEY"),
        "type" : 9,
        "number" : phone,
        "msg" : text
    }
    request_post = requests.post(url=SMS_URI, data=data)
    if(request_post.status_code==200):
        return True
    else:
        return False
          