city = {
    'Brasil':'Brasília',
    'Argetina': 'Buenos Aires',
    'Chile': 'Santiago',
    'Australia': 'Canberra',
    'Canada': 'Ottawa'
}

country_user = input('Insert Country')
if country_user in city:
    print(f'A Capital de {country_user} e {city[country_user]}')
else:
    print("Não Encontrado")