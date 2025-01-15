from numbers import Number


while True:
    IDkood = None
    FirstNumber = ['1','2','3','4','5','6']
    while IDkood is None:
        IDkoodtest = input('Enter ID kood: ')
        if IDkoodtest.isdigit() == True:
            if len(IDkoodtest) == 11:
                if IDkoodtest[0] in FirstNumber:
                   NumbersTest = IDkoodtest[1:3]
                   NumbersTest = int(NumbersTest)
                   if NumbersTest >= 0 and NumbersTest < 26:
                       NumbersTest = IDkoodtest[3:5]
                       NumbersTest = int(NumbersTest)                      
                       if NumbersTest > 0 and NumbersTest < 13:
                           NumbersTest = IDkoodtest[5:7]
                           NumbersTest = int(NumbersTest)
                           if NumbersTest > 0 and NumbersTest < 32:
                               pass
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
    