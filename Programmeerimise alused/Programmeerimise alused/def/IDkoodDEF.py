from IDkoodModul import *
ikoodid = []
arvud = []
IDkood = None

while IDkood is None:
    IDkoodtest = input('Enter ID kood: ')
    if IDkoodtest.isdigit() and validate_id(IDkoodtest, year, month, day):
        KontrollSumTest = calculate_control_sum(IDkoodtest)
        remainderOfKontrollSum = KontrollSumTest % 11
        if int(IDkoodtest[10]) == remainderOfKontrollSum:
            ikoodid.append(IDkoodtest)
            birthplace = determine_birthplace(IDkoodtest[7:10])
            if birthplace != 'Error Birth Place':
                sex = 'Female' if int(IDkoodtest[0]) % 2 == 0 else 'Male'
                if IDkoodtest[0] in ['3', '4']:
                    DateBirth = f"{IDkoodtest[5:7]}.{IDkoodtest[3:5]}.19{IDkoodtest[1:3]}"
                elif IDkoodtest[0] in ['5', '6']:
                    DateBirth = f"{IDkoodtest[5:7]}.{IDkoodtest[3:5]}.20{IDkoodtest[1:3]}"
                print(f"It's {sex} Date of Birthday {DateBirth} Place of Birth {birthplace}")
            else:
                print('Error Birth Place')
                arvud.append(IDkoodtest)
        else:
            print('Error Kontroll sum')
            arvud.append(IDkoodtest)
    else:
        print('Invalid ID Kood')
        arvud.append(IDkoodtest)

    quitvariable = input("Write Q if you want end programm. If you don't press Enter")
    if quitvariable in ['Q', 'q']:
        IDkood = 1
        arvud.sort()
        print('Not correct IDkodes', arvud)
        M, W = [], []
        for tempID in ikoodid:
            if tempID[0] in ['1', '3', '5']:
                M.append(tempID)
            elif tempID[0] in ['2', '4', '6']:
                W.append(tempID)
        print('Women ID kodes', W)
        print("Men ID kodes", M)
