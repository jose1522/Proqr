roles = {
    'Buyer' : 1,
    'Chief Approver' : 2,
    'Financial Approver' : 3
}

def roleStringToNumber(role):
    for key in roles:
        if (role == key):
            return roles[key]

def roleNumberToString(role):
    for key in roles:
        if (roles[key] == role):
            return key