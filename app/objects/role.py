
#roles es un diccionario que ayuda a la interacción entre el front end y la base de datos
#esto se debe a que en la base cada rol se guarda con un número que tiene asociado
roles = {
    'Buyer' : 1,
    'Financial Approver' : 2,
    'Chief Approver' : 3
}

#convierte el role de string a numero para guardarlo en la base

def roleStringToNumber(role):
    for key in roles:
        if (role == key):
            return roles[key]

#convierte el role de numero a string para desplegarlo en el combo
def roleNumberToString(role):
    for key in roles:
        if (roles[key] == role):
            return key

#get de los roles
def getRoles():
    return roles