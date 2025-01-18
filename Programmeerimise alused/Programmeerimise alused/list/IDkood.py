IDkood = None
FirstNumber = ['1','2','3','4','5','6']
FirstNumbertest = ['1','2','3','4']
Place = ['Kuressaare haigla', 'Tartu Ülikooli Naistekliinik', 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)', 'Keila haigla', 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)', 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)', 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla', 'Narva haigla', 'Pärnu haigla', 'Haapsalu haigla', 'Järvamaa haigla (Paide)', 'Rakvere haigla, Tapa haigla', 'Valga haigla', 'Viljandi haigla', 'Lõuna-Eesti haigla (Võru), Põlva haigla']
ikoodid = []
arvud = []
# Закончи момент с выходом и отсортируй списки
while IDkood is None:
    KontrollSumTest = 0
    IDkoodtest = input('Enter ID kood: ')
    if IDkoodtest.isdigit() == True:
        if len(IDkoodtest) == 11:
            if IDkoodtest[0] in FirstNumber:
                NumbersTest = IDkoodtest[1:3]
                NumbersTest = int(NumbersTest)
                FirstNumbervariable = IDkoodtest[0]
                if (NumbersTest >= 0 and NumbersTest < 26) or (NumbersTest >= 0 and NumbersTest < 100 and FirstNumbervariable in FirstNumbertest):
                    NumbersTest = IDkoodtest[3:5]
                    NumbersTest = int(NumbersTest)                      
                    if NumbersTest > 0 and NumbersTest < 13:
                        NumbersTest = IDkoodtest[5:7]
                        NumbersTest = int(NumbersTest)
                        if NumbersTest > 0 and NumbersTest < 32:
                            lastnumberID = IDkoodtest[10]
                            lastnumberID = int(lastnumberID)
                            if lastnumberID != 0:
                                for x in range(10):
                                    NumbersTest = IDkoodtest[x-1]
                                    NumbersTest = int(NumbersTest)
                                    KontrollSumTest = (NumbersTest * x) + KontrollSumTest
                                else:
                                    NumbersTest = IDkoodtest[9]
                                    NumbersTest = int(NumbersTest)
                                    KontrollSumTest = KontrollSumTest + NumbersTest
                            elif lastnumberID == 0:
                                for x in range(8):
                                    NumbersTest = IDkoodtest[x-1]
                                    NumbersTest = int(NumbersTest)
                                    KontrollSumTest = (NumbersTest * (x+2)) + KontrollSumTest
                                else:
                                    for x in range(4):
                                        NumbersTest = IDkoodtest[x+6]
                                        NumbersTest = int(NumbersTest)
                                        KontrollSumTest = (NumbersTest * x) + KontrollSumTest
                            remainderOfKontrollSum = float(KontrollSumTest % 11)
                            if lastnumberID == remainderOfKontrollSum:
                                ikoodid.append(IDkoodtest)
                                birthplace = IDkoodtest[7:10]
                                birthplace = int(birthplace)
                                if birthplace >= 1 and birthplace < 11:
                                    birthplace = Place[0]
                                elif birthplace >= 11 and birthplace < 21:
                                    birthplace = Place[1]
                                elif birthplace >= 21 and birthplace < 151:
                                    birthplace = Place[2]
                                elif birthplace >= 151 and birthplace < 161:
                                    birthplace = Place[3]
                                elif birthplace >= 161 and birthplace < 221:
                                    birthplace = Place[4]
                                elif birthplace >= 221 and birthplace < 271:
                                    birthplace = Place[5]
                                elif birthplace >= 271 and birthplace < 371:
                                    birthplace = Place[6]
                                elif birthplace >= 371 and birthplace < 421:
                                    birthplace = Place[7]
                                elif birthplace >= 421 and birthplace < 471:
                                    birthplace = Place[8]
                                elif birthplace >= 491 and birthplace < 521:
                                    birthplace = Place[9]
                                elif birthplace >= 521 and birthplace < 571:
                                    birthplace = Place[10]
                                elif birthplace >= 571 and birthplace < 601:
                                    birthplace = Place[11]
                                elif birthplace >= 601 and birthplace < 651:
                                    birthplace = Place[12]
                                elif birthplace >= 651 and birthplace < 701:
                                    birthplace = Place[13]
                                else:
                                    print('Error Birth Place')
                                    arvud.append(IDkoodtest)
                                sex = IDkoodtest[0]
                                sex = int(sex)
                                if sex % 2 == 0:
                                    sex = 'Female'
                                else:
                                    sex = 'Male'
                                if IDkoodtest[0] == '3' or IDkoodtest[0] == '4':
                                    DateBirth = IDkoodtest[5:7] + '.' + IDkoodtest[3:5] + '.' + '19' + IDkoodtest[1:3]
                                elif IDkoodtest[0] == '5' or IDkoodtest[0] == '6':
                                    DateBirth = IDkoodtest[5:7] + '.' + IDkoodtest[3:5] + '.' + '20' + IDkoodtest[1:3]
                                print(f"It's {sex} Date of Birthday {DateBirth} Place of Birth {birthplace}")

                            else:
                                print('Error Kontroll sum')
                                arvud.append(IDkoodtest)
                        else:
                            print('Error 6-7 numbers')
                            arvud.append(IDkoodtest)
                    else:
                        print('Error 4-5 numbers')
                        arvud.append(IDkoodtest)
                else:
                    print('Error 2-3 numbers')
                    arvud.append(IDkoodtest)
            else:
                print(IDkoodtest[0])
                print('ID kood only can start form ', FirstNumber )
                arvud.append(IDkoodtest)
        else:
            print('ID kood is not correct 11 numbers')
            arvud.append(IDkoodtest)
    else:
        print('ID kood is not correct ONLY INT')
    try:
        quitvariable = input("Write Q if you want end programm. If you don't press Enter")
    except:
        pass
    if quitvariable == 'Q' or quitvariable == 'q':
        IDkood = 1
        arvud.sort()
        print('Not correct IDkodes', arvud)
