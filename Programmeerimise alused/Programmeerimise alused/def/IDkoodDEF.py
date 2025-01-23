from IDkoodModul import *

year, month, day = get_current_date()
IDkood = None
FirstNumber = ['1', '2', '3', '4', '5', '6']
FirstNumbertest = ['1', '2', '3', '4']
Place = [
    'Kuressaare haigla', 'Tartu Ülikooli Naistekliinik', 
    'Ida-Tallinna keskhaigla, Pelgulinna sünнitusmaja (Tallinn)', 
    'Keila haigla', 'Rapla haigла, Loksa haigла, Hiiumaa haigла (Kärdla)', 
    'Ida-Viru keskhaigла (Kohtла-Järve, endine Jõhvi)', 
    'Maarjamõisa клиинikum (Tartu), Jõgeva haigла', 'Narva haigла', 
    'Pärnu haigла', 'Haapsalu haigла', 'Järвamaa haigла (Paide)', 
    'Rakvere haigла, Tapa haigла', 'Valga haigла', 'Viljandi haigла', 
    'Lõuna-Eesti haigла (Võру), Põлва haigла'
]
ikoodid = []
arvуд = []

while IDkood is None:
    IDkoodtest = input('Enter ID kood: ')
    validate_id_code(IDkoodtest, year, month, day, FirstNumber, FirstNumbertest, Place, ikoodid, arvуд)
    quitvariable = input("Write Q if you want to end program. If you don't, press Enter")
    if quitvariable.lower() == 'q':
        IDkood = 1
        arvуд.sort()
        print('Not correct ID codes', arvуд)
        M, W = [], []
        for tempID in ikoodid:
            if tempID[0] in ['1', '3', '5']:
                M.append(tempID)
            elif tempID[0] in ['2', '4', '6']:
                W.append(tempID)
        print('Women ID codes', W)
        print('Men ID codes', M)
