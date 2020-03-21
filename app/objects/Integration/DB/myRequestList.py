import requests
import json
from app.objects.Integration.DB.readKey import readDBKey
from app.objects.purchaseRequest import PurchaseRequest

#Metodo que trae los datos de la base de datos de los usuarios ya registrados en la aplicacion.
#Trae desde la base de datos todos los requests para un usuario específico

class MyRequestList:

    def __init__(self, user = 0):
        self.purchases = []
        self.user = user

    def FetchPurchaseList(self):
        key = readDBKey()

        #Tiene que cambiar
        url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.oraclecloudapps.com/ords/tables/api/my_requests"

        headers = {
            'Authorization': "Basic {0}".format(key),
            'X-ID': "{0}".format(self.user)
        }


        response = requests.request("GET", url, headers=headers)
        response = json.loads(response.text)

        if response['count'] > 0:
            items = response['items']
            for item in items:
                purchaseid = item['id']
                userid = item['employee']
                description = item['description']
                items = item['items']
                comments = item['comments']
                status = item['status']
                amount = item['amount']
                supervisor = item['supervisor']
                approver = item['approver']
                date = item['request_date']
                purchase = PurchaseRequest(requestid=purchaseid, userid=userid, description=description, items=items,
                                           comments=comments, amount=amount, status=status, supervisor=supervisor,
                                           approver=approver, date=date)
                self.purchases.append(purchase)
