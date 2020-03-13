import requests
import json
from app.objects.Integration.DB.readKey import readDBKey
from app.objects.purchaseRequest import PurchaseRequest

#Metodo que trae los datos de la base de datos de los usuarios ya registrados en la aplicacion.
class RequestList:

    def __init__(self):
        self.purchases = []

    def FetchPurchaseList(self):
        key = readDBKey()

        #Tiene que cambiar
        url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.oraclecloudapps.com/ords/tables/api/my_requests"

        headers = {
            'Authorization': "Basic {0}".format(key)
        }


        response = requests.request("GET", url, headers=headers)
        response = json.loads(response.text)

        if response['count'] > 0:
            items = response['items']
            for item in items:
                purchaseid = item['id']
                #description = item['description']
                #items = item['items']
                #comments = item['comments']
                #amount = item['amount']
                #purchase = PurchaseRequest(requestid=purchaseid, description=description, items=items,
                #                           comments=comments, amount=amount)
                purchase = PurchaseRequest(requestid=purchaseid)
                self.purchases.append(purchase)
