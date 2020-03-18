import requests
from app.objects.sendGrid import SendEmail
from app.objects.Integration.DB.readKey import readDBKey
import json

#Metodo para agregar el contenido a la base de datos (Solicitudes con sus parametros)
def AddRequest(purchaseRequest, userEmail):
    key = readDBKey()

    url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.oraclecloudapps.com/ords/tables/api/request"

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
    if response.status_code == 200:

        serverOutput = json.loads(response.text)
        supervisorEmail = serverOutput['X-SUPERVISOR']
        requestID = serverOutput['X-RESQUEST_ID']

        body = """Your request has been placed succesfully!\n\n 
                PROQR\n
                This e-mail message has been delivered from a send-only address. Please do not reply to this message.""".format(requestID)
        SendEmail(sender='noreply@email.com', to=userEmail, subject='Purchase Request {0} Confirmation'.format(requestID), body=body)


        body = """A new request has been submitted for approval: {0}\n\n 
                  'PROQR\n'
                  This e-mail message has been delivered from a send-only address. Please do not reply to this message.
                """.format(requestID)

        SendEmail(sender='noreply@email.com', to=supervisorEmail, subject='Purchase Request Confirmation',body=body)

    return response.status_code