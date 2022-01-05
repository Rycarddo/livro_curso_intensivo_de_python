def build_profile(first, last, **another_informations):
    profile = {'first_name': first, 'last_name': last}
    for key, value in another_informations.items():
        profile[key] = value
    return profile


user = build_profile('Isaac', 'Newton', curso='Física', apelido='Homem que criou o cálculo')
print(user)