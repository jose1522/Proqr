import requests
from app.objects.sendGrid import SendEmail
from app.objects.Integration.DB.readKey import readDBKey
from app.objects.newPassword import CreatePassword

#Metodo para agregar el contenido a la base de datos (Usarios con sus parametros)
def AddUser(user):
    key = readDBKey()

    url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.oraclecloudapps.com/ords/tables/api/users"
    password = CreatePassword()
    headers = {
        'X-NAME': user.firstName,
        'X-LAST': user.lastName,
        'X-EMAIL': user.email,
        'X-PASSWORD': password,
        'X-ROLE': str(user.role),

        'Authorization': "Basic {0}".format(key)
    }

    response = requests.request("POST", url, headers=headers)
    #Envio del password al usuario atraves de correo electornico
    body = 'Your PROQR password is {0}'.format(password)
    SendEmail(sender='noreply@email.com', to=user.email, subject='Welcome to PROQR',body=body)
    return response.status_code