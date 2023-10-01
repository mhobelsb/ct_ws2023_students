print('Geben Sie das Kürzel Ihres Studiengang ein und bestätigen Sie mit [Enter]:')
major = input().lower()

print('Geben Sie ihr Alter ein und bestätigen die Eingabe mit [Enter]:')
age = int(input())

if major == 'gs':
    print(f'Sie sind {age} Jahre alt und studieren Geodata Science!')
    print('Willkommen an der Studienfakultät MUC.DAI')
elif major == 'de':
    print(f'Sie sind {age} Jahre alt und studieren Digital Engineering!')
    print('Willkommen an der Studienfakultät MUC.DAI')
else:
    print(f'\"{major}\" ist mir unbekannt. Sind Sie hier richtig?')