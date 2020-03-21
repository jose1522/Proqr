import requests
import json
from app.objects.Integration.DB.readKey import readDBKey

#Metodo para modificar el contenido en la base de datos (Usarios con sus parametros)
#Permite verificar si el usuario es un administrador
def IsAdmin(userId):
    key = readDBKey()

    url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.oraclecloudapps.com/ords/tables/api/is_admin"

    headers = {
        'X-ID': str(userId),
        'Authorization': "Basic {0}".format(key)
    }

    response = requests.request("GET", url, headers=headers)
    response = json.loads(response.text)
    if response['admin'] == 1:
        return True
    else:
        return False




