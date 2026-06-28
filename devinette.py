import random
a = 1
b = 20
nombre = random.randint(a, b)
essais = 0
guess = 0
while guess != nombre:
    print('devine le nombre qui est entre ' + str(a) + ' et ' + str(b-1))
    guess = int(input('>'))
    essais += 1
    if (guess < nombre):
        print('trop petit')
    elif (guess > nombre):
        print ('trop grand')
    else: 
        print('tu as trouvé le bon nombre en ' + str(essais) + ' essais') 
