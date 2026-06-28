
def addition(a, b):
    return a + b
def soustraction(a, b):
    return a-b
def multiplication(a, b):
    return a * b
def division(a,b):
    try:
        return a /b
    except ZeroDivisionError:
        print('division by zero')
        return None

print('1 : pour addition')
print('2 : pour soustraction')
print('3 : pour multiplication')
print('4 : pour division')

choix = input('>')

a = float(input("Premier nombre : "))
b = float(input("Deuxième nombre : "))

if (choix == '1'):
    print(addition(a,b))
elif (choix == '2'):
    print(soustraction(a,b))
elif (choix == '3'):
    print(multiplication(a, b))
elif (choix == '4'):
    print(division(a, b))
else:
    print('mauvais choix')