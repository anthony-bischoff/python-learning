# ce code calcule une moyenne selon le nombre de crédit et les notes
print('conmbien de cours as-tu? ')
nb_cours = int(input('>'))
credit_tot = 0
note_tot = 0
for i in range(nb_cours):
    print('combien de crédit pour le cours no' + str(i+1))
    credit = int(input('>'))
    print('quelle note as tu obtenu pour le cours no' + str(i+1))
    note = float(input('>'))
    credit_tot += credit
    note_tot += note*credit
moyenne = note_tot / credit_tot
print('ta moyenne est : ' + str(round(moyenne, 2)))
if (moyenne < 4.0):
    print('tu as échoué')
else: 
    print("bravo tu as passé ton année")