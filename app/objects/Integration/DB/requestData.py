import requests
import json
from app.objects.Integration.DB.readKey import readDBKey
from app.objects.purchaseRequest import PurchaseRequest

#Metodo para traer los datos de la bases de datos, para rellenar el formulario ya existentes
#Permite obtener información de un request

def FetchPurchaseData(id=0):
    key = readDBKey()

    url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.oraclecloudapps.com/ords/tables/api/request"

    headers = {
        'X-ID': str(id),
        'Authorization': "Basic {0}".format(key)
    }

    response = requests.request("GET", url, headers=headers)
    response = json.loads(response.text)

    if response['count'] > 0:
        response = response['items']
        response = response[0]
        purchaseid = response['id']
        userid = response['employee']
        description = response['description']
        try:
            items = json.loads(response['items'])
        except:
            items = response['items']

        try:
            comments = json.loads(response['comments'])
        except:
            comments = response['comments']
        status = response['status']
        amount = response['amount']
        supervisor = response['supervisor']
        approver = response['approver']
        date = response['request_date']
        purchase = PurchaseRequest(requestid=purchaseid, userid=userid ,description=description, items=items,
                                   comments=comments, amount=amount, status=status, supervisor=supervisor,
                                   approver=approver, date=date)
        return purchase
    else:
        return PurchaseRequest()
