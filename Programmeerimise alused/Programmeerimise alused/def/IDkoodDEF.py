from datetime import date
from IDkoodModul import *
current_date = date.today()
year, month, day = current_date.year, current_date.month, current_date.day
FirstNumber = ['1','2','3','4','5','6']
FirstNumbertest = ['1','2','3','4']
Place = ['Kuressaare haigla', 'Tartu Ülikooli Naistekliinik', 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)', 'Keila haigla', 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)', 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)', 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla', 'Narva haigla', 'Pärnu haigla', 'Haapsalu haigla', 'Järvamaa haigla (Paide)', 'Rakvere haigla, Tapa haigla', 'Valga haigla', 'Viljandi haigla', 'Lõuna-Eesti haigla (Võru), Põlva haigla']
ikoodid = []
arvud = []
exitt = None
while exitt == None:
    try:
        quitvariable = input("Write Q if you want end programm. If you don't press Enter")
    except:
        pass
    if quitvariable == 'Q' or quitvariable == 'q':
        arvud.sort()
        quantityOfArvudinList = len(arvud)
        if quantityOfArvudinList == 0:
            print('List "arvud" is empty')
        else:
            print('Not correct IDkodes', arvud)
        quantityOfIDinList = len(ikoodid)
        if quantityOfIDinList == 0:
            print('List "ikoodid" is empty')
        else:
            M, W = [], []
            for x in range(quantityOfIDinList):
                tempID = ikoodid[x]
                if tempID[0] in ['1', '3', '5']:
                    M.append(tempID)
                elif tempID[0] in ['2', '4', '6']:
                    W.append(tempID)
                print('Women ID kodes', W)
                print("Men ID kodes", M)
        break
    IDkoodtest = input('Enter ID kood: ')
    if validate_id_code(IDkoodtest, year, month, day, FirstNumber, FirstNumbertest) == True:
        if checksum(IDkoodtest) == True:
            birthplace = birtplacedef(IDkoodtest)
            sex = sexdef(IDkoodtest)
            dateofbirth = dateofbirthdef(IDkoodtest)
            ikoodid.append(IDkoodtest)
            print(f"It's {sex} Date of Birthday {dateofbirth} Place of Birth {Place[birthplace]}")
        else:
            arvud.append(IDkoodtest)
    else:
        arvud.append(IDkoodtest)
