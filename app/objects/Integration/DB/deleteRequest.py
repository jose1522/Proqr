import requests
from app.objects.Integration.DB.readKey import readDBKey

#Metodo para borrar el contenido en la base de datos (Solicitudes con sus parametros)
#Manda un request de delete a la base de datos, cambia el estado del request
def DeleteRequest(purchaseRequest):
    key = readDBKey()

    url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.oraclecloudapps.com/ords/tables/api/request"

    headers = {
        #Recibe el ID del request que va ser borrado
        'X-ID': purchaseRequest.requestid,

        'Authorization': "Basic {0}".format(key)
    }

    response = requests.request("DELETE", url, headers=headers)
    return response.status_code