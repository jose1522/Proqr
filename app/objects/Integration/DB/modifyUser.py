import requests
from app.objects.Integration.DB.readKey import readDBKey

#Metodo para modificar el contenido en la base de datos (Usarios con sus parametros)
#Se encarga de modidicar el usuario

def ModifyUser(user):
    key = readDBKey()

    url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.oraclecloudapps.com/ords/tables/api/users"

    headers = {
        'X-ID': user.userId,
        'X-NAME': user.firstName,
        'X-LAST': user.lastName,
        'X-EMAIL': user.email,
        'X-ROLE': str(user.role),
        'X-STATUS': user.status,


        'Authorization': "Basic {0}".format(key)
    }

    response = requests.request("POST", url, headers=headers)
    return response.status_code




