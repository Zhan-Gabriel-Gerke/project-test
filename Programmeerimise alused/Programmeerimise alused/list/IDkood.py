while True:
    IDkood = None
    FirstNumber = ['1','2','3','4','5','6']
    FirstNumberstest = ['1','2','3','4']
    KontrollSumTest = 0
    while IDkood is None:
        IDkoodtest = input('Enter ID kood: ')
        if IDkoodtest.isdigit() == True:
            if len(IDkoodtest) == 11:
                if IDkoodtest[0] in FirstNumber:
                   NumbersTest = IDkoodtest[1:3]
                   NumbersTest = int(NumbersTest)# Тут проблема снизу на 13 сторке 37605030270
                   if (NumbersTest >= 0 and NumbersTest < 26) or (NumbersTest >= 0 and NumbersTest < 100 and FirstNumber in FirstNumberstest):
                       NumbersTest = IDkoodtest[3:5]
                       NumbersTest = int(NumbersTest)                      
                       if NumbersTest > 0 and NumbersTest < 13:
                           NumbersTest = IDkoodtest[5:7]
                           NumbersTest = int(NumbersTest)
                           if NumbersTest > 0 and NumbersTest < 32:
                               for x in range(10):
                                   NumbersTest = IDkoodtest[x-1]
                                   NumbersTest = int(NumbersTest)
                                   KontrollSumTest = (NumbersTest * x) + KontrollSumTest
                               else:
                                   NumbersTest = IDkoodtest[9]
                                   NumbersTest = int(NumbersTest)
                                   KontrollSumTest = KontrollSumTest + NumbersTest
                                   print('Kontroll Sum: ', KontrollSumTest)
                               if KontrollSumTest % 11 == 10:
                                   KontrollSumTest = 0
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
                                           print('Kontroll sum II', KontrollSumTest)
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
    