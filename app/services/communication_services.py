import json
from os import getenv

from aiohttp import ClientSession


async def sms_send(phone: str, text: str):

    SMS_URI = "https://api.smsdev.com.br/v1/send"

    data = {"key": getenv("SMS_URI_KEY"), "type": 9, "number": phone, "msg": text}

    async with ClientSession() as client_session:
        async with client_session.post(SMS_URI, data=data) as response:
            response = await response.read()
    response = json.loads(response.decode("utf-8"))

    return response
