import requests
import json
from app.objects.Integration.DB.readKey import readDBKey
from app.objects.user import User


class UserList:

    def __init__(self):
        self.users = []

    def FetchUserList(self):
        key = readDBKey()

        url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.oraclecloudapps.com/ords/tables/api/user_list"

        headers = {
            'Authorization': "Basic {0}".format(key)
        }


        response = requests.request("GET", url, headers=headers)
        response = json.loads(response.text)

        if response['count'] > 0:
            items = response['items']
            for item in items:
                id = item['id']
                name = item['name']
                lastName = item['last']
                email = item['email']
                role = item['role']
                user = User(userid=id, firstname=name, lastname=lastName, email=email, role=role)
                self.users.append(user)


