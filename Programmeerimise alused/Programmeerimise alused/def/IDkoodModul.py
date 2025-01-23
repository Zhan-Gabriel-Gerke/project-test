from datetime import date

def get_current_date():
    current_date = date.today()
    return current_date.year, current_date.month, current_date.day

def validate_id_length(IDkoodtest):
    return len(IDkoodtest) == 11

def validate_first_number(IDkoodtest, FirstNumber):
    return IDkoodtest[0] in FirstNumber

def calculate_kontrollsum(IDkoodtest):
    KontrollSumTest = 0
    for x in range(10):
        NumbersTest = int(IDkoodtest[x])
        KontrollSumTest += NumbersTest * ((x % 9) + 1)
    remainderOfKontrollSum = KontrollSumTest % 11
    if remainderOfKontrollSum == 10:
        KontrollSumTest = 0
        for x in range(8):
            NumbersTest = int(IDkoodtest[x])
            KontrollSumTest += NumbersTest * ((x % 8) + 2)
        remainderOfKontrollSum = KontrollSumTest % 11
    return remainderOfKontrollSum

def determine_birthplace(birthplace, Place):
    for index, threshold in enumerate(range(1, 701, 50)):
        if birthplace < threshold + 50:
            return Place[index]
    return "Unknown"

def determine_sex(IDkoodtest):
    return "Female" if int(IDkoodtest[0]) % 2 == 0 else "Male"

def determine_date_of_birth(IDkoodtest):
    century_prefix = "19" if IDkoodtest[0] in ['3', '4'] else "20"
    return f"{IDkoodtest[5:7]}.{IDkoodtest[3:5]}.{century_prefix}{IDkoodtest[1:3]}"

def validate_id_code(IDkoodtest, year, month, day, FirstNumber, FirstNumbertest, Place, ikoodid, arvud):
    if IDkoodtest.isdigit():
        if validate_id_length(IDkoodtest):
            if validate_first_number(IDkoodtest, FirstNumber):
                NumbersTesty = int(IDkoodtest[1:3])
                FirstNumbervariable = IDkoodtest[0]
                if (NumbersTesty >= 0 and NumbersTesty <= year) or (
                    NumbersTesty >= 0 and NumbersTesty < 100 and 
                    FirstNumbervariable in FirstNumbertest):
                    NumbersTestM = int(IDkoodtest[3:5])
                    if (NumbersTesty == year and NumbersTestM <= month) or (
                        NumbersTestM > 0 and NumbersTestM < 13):
                        NumbersTest = int(IDkoodtest[5:7])
                        if (NumbersTesty == year and NumbersTest == month and NumbersTest <= day) or (
                            NumbersTest > 0 and NumbersTest < 32):
                            remainderOfKontrollSum = calculate_kontrollsum(IDkoodtest)
                            lastnumberID = int(IDkoodtest[10])
                            if lastnumberID == remainderOfKontrollSum:
                                ikoodid.append(IDkoodtest)
                                birthplace = int(IDkoodtest[7:10])
                                birthplace_str = determine_birthplace(birthplace, Place)
                                sex = determine_sex(IDkoodtest)
                                DateBirth = determine_date_of_birth(IDkoodtest)
                                print(f"It's {sex} Date of Birthday {DateBirth} Place of Birth {birthplace_str}")
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
                print('ID kood only can start from', FirstNumber)
                arvud.append(IDkoodtest)
        else:
            print('ID kood is not correct 11 numbers')
            arvud.append(IDkoodtest)
    else:
        print('ID kood is not correct ONLY INT')
