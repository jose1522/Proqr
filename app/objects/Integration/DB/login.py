import requests
import json
from app.objects.Integration.DB.readKey import readDBKey
import hashlib


class UserLogin:

    def __init__(self, password=None, email=None):
        self.__email = email
        self.__password = password  # to do add hashing to password
        self.id = 0

    def SetPassword(self, password):
        self.__password = password

    def SetEmail(self, email):
        self.__email = email

    def Authenticate(self):

        key = readDBKey()

        url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.oraclecloudapps.com/ords/tables/api/authenticate"

        headers = {
            'X-Password': self.__password,
            'X-Email': self.__email,
            'Authorization': "Basic {0}".format(key)
        }

        response = requests.request("GET", url, headers=headers)
        response = json.loads(response.text)
        return response

    def __HashString(self, inputString):
        return hashlib.sha3_512(inputString)

