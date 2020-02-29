import requests
from app.objects.sendGrid import SendEmail
from app.objects.Integration.DB.readKey import readDBKey
from app.objects.newPassword import CreatePassword

def RecoverPassword(user):
    key = readDBKey()

    url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.oraclecloudapps.com/ords/tables/api/recover_password"
    headers = {
        'Authorization': "Basic {0}".format(key)
    }
    password = CreatePassword()
    if user.userId != "":
        headers.update({"X-ID":user.userId})
        headers.update({"X-Password": password})
    elif user.email != "":
        headers.update({"X-Email": user.email})
        headers.update({"X-Password": password})

    SendEmail(sender='noreply@email.com', to= user.email,subject='Your New Password', body= password)
    response = requests.request("PUT", url, headers=headers)
    return response.status_code




