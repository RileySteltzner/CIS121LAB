def access_rights(user_role):
    if user_role == 'guest':
        return 'View only access'
    elif user_role == 'user':
        return 'Limited access'
    else:
        if user_role == 'admin':
            return 'Full access'
print(access_rights('admin'))