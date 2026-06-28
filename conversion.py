def celsius_far(c):
    return (c * 9/5) + 32
def km_miles(km):
    return km * 0.621371
def kg_livres(kg):
    return kg * 2.20462

print('Quelle conversion veux-tu faire ?')
print('1) Celsius en Fahrenheit')
print('2) Km en Miles')
print('3) Kg en Livres')
choix =  input('>')

a = float(input("Valeur à convertir"))

if (choix == '1'):
    print(str(a) + '°C = ' + str(celsius_far(a)) + '°F')
elif (choix == '2'):
    print(str(a) + ' km = ' + str(km_miles(a)) + ' miles')
elif (choix == '3'):
    print(str(a) + ' kg = ' + str(kg_livres(a)) + ' livres')
else:
    print('mauvais choix')