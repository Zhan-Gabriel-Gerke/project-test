def validate_id_code(IDkoodtest, year, month, day, FirstNumber, FirstNumbertest):
    if IDkoodtest.isdigit() and len(IDkoodtest) == 11:
        if IDkoodtest[0] in FirstNumber:
            NumbersTesty = int(IDkoodtest[1:3])
            FirstNumbervariable = IDkoodtest[0]
            
            if (0 <= NumbersTesty <= year) or (0 <= NumbersTesty < 100 and FirstNumbervariable in FirstNumbertest):
                NumbersTestM = int(IDkoodtest[3:5])
                
                if (NumbersTesty == year and NumbersTestM <= month) or (0 < NumbersTestM < 13):
                    NumbersTestD = int(IDkoodtest[5:7])
                    
                    if (NumbersTesty == year and NumbersTestM == month and NumbersTestD <= day) or (0 < NumbersTestD < 32):
                        return True
    return False
def checksum(IDkoodtest):
    lastnumberID = int(IDkoodtest[10])
    KontrollSumTest = 0
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
    else:
        print('Error Kontroll sum')
        return False
    remainderOfKontrollSum = float(KontrollSumTest % 11)
    if lastnumberID == remainderOfKontrollSum:
        return True
    else:
        return False

def birtplacedef (IDkoodtest):
    birthplace = IDkoodtest[7:10]
    birthplace = int(birthplace)
    if birthplace >= 1 and birthplace < 11:
        birthplace = 0
    elif birthplace >= 11 and birthplace < 21:
        birthplace = 1
    elif birthplace >= 21 and birthplace < 151:
        birthplace = 2
    elif birthplace >= 151 and birthplace < 161:
        birthplace = 3
    elif birthplace >= 161 and birthplace < 221:
        birthplace = 4
    elif birthplace >= 221 and birthplace < 271:
        birthplace = 5
    elif birthplace >= 271 and birthplace < 371:
        birthplace = 6
    elif birthplace >= 371 and birthplace < 421:
        birthplace = 7
    elif birthplace >= 421 and birthplace < 471:
        birthplace = 8
    elif birthplace >= 491 and birthplace < 521:
        birthplace = 9
    elif birthplace >= 521 and birthplace < 571:
        birthplace = 10
    elif birthplace >= 571 and birthplace < 601:
        birthplace = 11
    elif birthplace >= 601 and birthplace < 651:
        birthplace = 12
    elif birthplace >= 651 and birthplace < 701:
        birthplace = 13
    else:
        birthplace = 100
    return birthplace

def sexdef(IDkoodtest):
    sex = int(IDkoodtest[0])
    if sex % 2 == 0:
        sex = 'Female'
    else:
        sex = 'Male'
    return sex
def dateofbirthdef(IDkoodtest):
    if IDkoodtest[0] == '3' or IDkoodtest[0] == '4':
        DateBirth = IDkoodtest[5:7] + '.' + IDkoodtest[3:5] + '.' + '19' + IDkoodtest[1:3]
    elif IDkoodtest[0] == '5' or IDkoodtest[0] == '6':
        DateBirth = IDkoodtest[5:7] + '.' + IDkoodtest[3:5] + '.' + '20' + IDkoodtest[1:3]
    return DateBirth