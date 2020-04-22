import requests
from app.objects.Integration.DB.notification import RequestNotification
from app.objects.Integration.DB.readKey import readDBKey
import json
import pandas as pd

class Stats:

    def __init__(self, role, userID):
        self.role = role
        self.userID = userID
        self.data = {}

    #Metodo para agregar el contenido a la base de datos (Solicitudes con sus parametros)
    #Método que agrega un request

    def GetData(self):
        return self.__TransformData()

    def __SendRequest(self):
        key = readDBKey()
        url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.oraclecloudapps.com/ords/tables/api/stats/"+ ("supervisor" if self.role == 2 else "approver")
        headers = {
            'X-ID': str(self.userID),
             'Authorization': "Basic {0}".format(key)
        }

        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return None

    def __TransformData(self):
        data = self.__SendRequest()
        if data:
            ranges = [3,6,12]
            status = ['Approved','Pending','Rejected']
            dataByRanges = {}
            df = pd.DataFrame(data['items'])
            for period in ranges:
                dataByRanges[period] = df[df['month']<=period]
            for key, value in dataByRanges.items():
                tempDict = {}
                value = df.rename(columns={"month": "x", "count": "y"})
                tempDict['RecievedChart'] = value.groupby(['x']).agg('sum').reset_index().drop(columns=['amount'], axis=1).to_dict('list')
                tempDict['RecievedSum'] = "${:,}".format(value['amount'].sum())
                tempDict['RecievedCount'] = value['y'].sum()

                for item in status:
                    filteredData = value[value['status']==item].drop('status', 1)
                    tempDict[item+'Chart'] = filteredData.groupby(['x']).agg('sum').reset_index().drop('amount', axis=1).to_dict('list')
                    tempDict[item + 'Sum'] = "${:,}".format(filteredData['amount'].sum())
                    tempDict[item + 'Count'] = filteredData['y'].sum()
                dataByRanges[key] = tempDict
            return dataByRanges
        else:
            return None

