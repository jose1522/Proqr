roles = {
    'Buyer' : 1,
    'Financial Approver' : 2,
    'Chief Approver' : 3
}

def roleStringToNumber(role):
    for key in roles:
        if (role == key):
            return roles[key]

def roleNumberToString(role):
    for key in roles:
        if (roles[key] == role):
            return key