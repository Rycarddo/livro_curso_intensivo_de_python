current_users = ['José', 'Rycarddo', 'Nascimento', 'Freitas', 'Tony']
current_users_lower = [current_user.lower() for current_user in current_users]
new_users = ['Rycarddo', 'Ezekyel', 'Jefferson', 'José', 'Sheila']
new_users_lower = [new_user.lower() for new_user in new_users]

for new_user_lower in new_users_lower:
    if new_user_lower in current_users_lower:
        print(f'{new_user_lower.title()}\nNome de usuário em uso, tente novamente.')
    else:
        print(f'{new_user_lower.title()}\nUsuário disponível.')
