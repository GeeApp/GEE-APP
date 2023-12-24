
def Is_Enseignants(user):
    return user.groups.filter(name = 'Enseignants').exists()

def Is_Administration(user):
    return user.groups.filter(name = 'Administration').exists()

def Is_Enseignants_nav(user):
    if user.groups.filter(name = 'Enseignants').exists():
        update = """ Mise à jour"""
        return  update