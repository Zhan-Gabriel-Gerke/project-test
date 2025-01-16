IDkood = None
FirstNumber = ['1','2','3','4','5','6']
FirstNumbertest = ['1','2','3','4']
ikoodid = []
arvud = []
while True:
    while IDkood is None:
        KontrollSumTest = 0
        IDkoodtest = input('Enter ID kood: ')
        if IDkoodtest.isdigit() == True:
            if len(IDkoodtest) == 11:
                if IDkoodtest[0] in FirstNumber:
                   NumbersTest = IDkoodtest[1:3]
                   NumbersTest = int(NumbersTest)# Тут проблема снизу на 13 сторке 37605030270 # Тут список в списке без цикла ищётся сделай переменную и норм будет
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
                                       print('Kontroll Sum: ', KontrollSumTest)
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
                                       else:
                                           print('Kontroll sum II Iteration', KontrollSumTest)
                               remainderOfKontrollSum = float(KontrollSumTest % 11)
                               if lastnumberID == remainderOfKontrollSum:
                                   ikoodid.append(IDkoodtest)
                                   print(ikoodid)
                                   print(f'It\'s {})
                               else:
                                   print('Error aadddd')
                               print(lastnumberID, 'ostaton ->', remainderOfKontrollSum)
                           else:
                               print('Error 6-7 numbers')
                       else:
                           print('Error 4-5 numbers')
                   else:
                       print('Error 2-3 numbers')
                else:
                    print(IDkoodtest[0])
                    print('ID kood only can start form ', FirstNumber )
            else:
                print('ID kood is not correct 11 numbers')
        else:
            print('ID kood is not correct ONLY INT')
    