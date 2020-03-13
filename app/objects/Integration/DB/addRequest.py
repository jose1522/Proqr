import requests
from app.objects.sendGrid import SendEmail
from app.objects.Integration.DB.readKey import readDBKey

#Metodo para agregar el contenido a la base de datos (Solicitudes con sus parametros)
def AddRequest(purchaseRequest, user):
    key = readDBKey()

    url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.addUser.pyoraclecloudapps.com/ords/tables/api/users"

    headers = {
        'X-ID': purchaseRequest.userid,
        'X-DESCRIPTION': purchaseRequest.description,
        'X-ITEMS': purchaseRequest.items,
        'X-COMMENTS': purchaseRequest.comments,
        'X-AMOUNT': purchaseRequest.amount,

        'Authorization': "Basic {0}".format(key)
    }

    response = requests.request("POST", url, headers=headers)
    #Envio de la confirmacion cuando el usuario hace un request atraves de correo electornico
    body = 'Your request has been placed succesfully!' \
           '' \
           'PROQR' \
           '' \
           'This e-mail message has been delivered from a send-only address. Please do not reply to this message.'
    SendEmail(sender='noreply@email.com', to=user.email, subject='Purchase Request Confirmation',body=body)
    return response.status_code