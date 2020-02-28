import requests
from app.objects.Integration.DB.readKey import readDBKey
from app.objects.newPassword import CreatePassword

def RecoverPassword(user):
    key = readDBKey()

    url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.oraclecloudapps.com/ords/tables/api/recover_password"
    headers = {
        'Authorization': "Basic {0}".format(key)
    }
    if user.userId != "":
        headers.update({"X-ID":user.userId})
        headers.update({"X-Password": CreatePassword()})
    elif user.email != "":
        headers.update({"X-Email": user.email})
        headers.update({"X-Password": CreatePassword()})

    response = requests.request("PUT", url, headers=headers)
    return response.status_code




