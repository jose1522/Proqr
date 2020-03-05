import secrets
import string

#Este método se encarga de crear una nueva contraseña de manera random, es
#la que se utiliza cuando al usuario se le ovlidad o cuando se crea un
#nuevo usuario

def CreatePassword(len=20):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(len))
    return password