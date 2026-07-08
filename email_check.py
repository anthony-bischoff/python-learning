mail = input("Entrez votre E-mail : ")
status = True
if '@' not in  mail:
    status = False
elif '.' not in mail:
    status = False
elif ' ' in mail:
    status = False
elif mail.startswith('@'):
    status = False
elif mail.endswith('@'):
    status = False

if status:
    print('Adresse valide')
else: 
    print('Adresse invalide')