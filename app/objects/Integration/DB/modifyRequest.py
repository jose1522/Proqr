import requests
from app.objects.sendGrid import SendEmail
from app.objects.Integration.DB.readKey import readDBKey

#Metodo para modificar el contenido en la base de datos (Solicitudes con sus parametros)
def ModifyRequest(purchaseRequest, user):
    key = readDBKey()

    url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.oraclecloudapps.com/ords/tables/api/users"

    headers = {
        'X-ID': purchaseRequest.requestid,
        'X-COMMENTS': purchaseRequest.comments,
        'X-STATUS': purchaseRequest.status,

        'Authorization': "Basic {0}".format(key)
    }

    response = requests.request("POST", url, headers=headers)
    #Envio de la confirmacion del cambio en el request al usuario atraves de correo electornico
    body = 'Your request has been updated successfully!' \
           '' \
           'PROQR' \
           '' \
           'This e-mail message has been delivered from a send-only address. Please do not reply to this message.'
    SendEmail(sender='noreply@email.com', to=user.email, subject='Request Update Confirmation',body=body)
    return response.status_code




