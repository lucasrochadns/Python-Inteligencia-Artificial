city = ['São Paulo', 'Belo Horizonte', 'Brasilía', 'Rio Janeiro']
city_user = input("Insira a cidade ")

if city_user in city:
    print(f" City is {city_user}")
else:
    print(f" City not on the list {city_user}")