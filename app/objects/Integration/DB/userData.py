import requests
import json
from app.objects.Integration.DB.readKey import readDBKey
from app.objects.user import User


def FetchUserData(id=0):
    key = readDBKey()

    url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.oraclecloudapps.com/ords/tables/api/users"

    headers = {
        'X-ID': str(id),
        'Authorization': "Basic {0}".format(key)
    }

    response = requests.request("GET", url, headers=headers)
    response = json.loads(response.text)

    if response['count'] > 0:
        item = response['items']
        item = item[0]
        name = item['name']
        lastName = item['lastname']
        email = item['email']
        role = item['role']
        user = User(userid=id, firstname=name, lastname=lastName, email=email, role=role)
        return user
    else:
        return User()


