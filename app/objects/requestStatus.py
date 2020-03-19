
#roles es un diccionario que ayuda a la interacción entre el front end y la base de datos
#esto se debe a que en la base cada rol se guarda con un número que tiene asociado
status = {
    'Awaiting supervisor approval' : 1,
    'Awaiting financial approval' : 2,
    'Approved' : 3,
    'Rejected' : 4
}

#convierte el role de string a numero para guardarlo en la base

def statusStringToNumber(status):
    for key in roles:
        if (status == key):
            return roles[key]

#convierte el role de numero a string para desplegarlo en el combo
def statusNumberToString(input):
    for key in status:
        if (status[key] == input):
            return key

#get de los roles
def getStatus():
    return status