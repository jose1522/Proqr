import requests
from app.objects.Integration.DB.readKey import readDBKey

#Metodo para borrar el contenido en la base de datos (Usarios con sus parametros)
def DeleteUser(user):
    key = readDBKey()

    url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.oraclecloudapps.com/ords/tables/api/users"

    headers = {
        #Recibe el ID del usuario que va ser borrado
        'X-ID': user.userId,

        'Authorization': "Basic {0}".format(key)
    }

    response = requests.request("DELETE", url, headers=headers)
    return response.status_code