import enum

from aiohttp import ClientSession
from .models import Balance, Status
from .exceptions import InvalidPhoneNumber


class RequestMethods(enum.StrEnum):
    POST = "POST"
    GET = "GET"
    PUT = "PUT"


class MoonheimSMS:
    BASE_URL = "https://moongateway.io/api/"

    def __init__(self, token: str, proxy: str = None):
        self.session = ClientSession()
        self.proxy = proxy
        self.token = token

    async def sendSms(self, phone: str, sender_name: str, text: str, type_: int = 0, gateway: int = 0,
                      short_link: int = 1):
        response = await self.__request(RequestMethods.POST, self.BASE_URL + "sms_send",
                                        json={"phone": phone, "sid": sender_name, "text": text, "type": type_,
                                              "gateway": gateway,
                                              "short_link": short_link})
        print(response)

    async def checkSmsStatus(self, message_id: str):
        response = await self.__request(RequestMethods.POST, self.BASE_URL + "check_dlr")
        return Status(**response)

    async def getBalance(self):
        response = await self.__request(RequestMethods.POST, self.BASE_URL + "check_balance")
        return Balance(**response)

    async def __request(self, method: RequestMethods, url: str, **args) -> dict:
        payload = {}
        args.get("json") and (payload := args.pop("json"))
        payload["token"] = self.token
        response = await self.session.request(method, url, proxy=self.proxy, json=payload, **args)
        jsoned: dict = await response.json()
        if jsoned.get("error"):
            error = jsoned.pop("error")
            if error == "Invalid phone number":
                raise InvalidPhoneNumber(error)
            raise Exception(error)
        return jsoned
