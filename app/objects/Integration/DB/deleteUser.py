import requests
from app.objects.Integration.DB.readKey import readDBKey


def DeleteUser(user):
    key = readDBKey()

    url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.oraclecloudapps.com/ords/tables/api/users"

    headers = {
        'X-ID': user.userId,

        'Authorization': "Basic {0}".format(key)
    }

    response = requests.request("DELETE", url, headers=headers)
    return response.status_code