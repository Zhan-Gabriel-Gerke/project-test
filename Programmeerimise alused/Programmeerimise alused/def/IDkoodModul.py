from datetime import date

# Общие переменные
current_date = date.today()
year, month, day = current_date.year, current_date.month, current_date.day
FirstNumber = ['1', '2', '3', '4', '5', '6']
FirstNumbertest = ['1', '2', '3', '4']
Place = [
    'Kuressaare haigla',
    'Tartu Ülikooli Naistekliinik',
    'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)',
    'Keila haigla',
    'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)',
    'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)',
    'Maarjamõisa kliinikum (Tartu), Jõgeva haigla',
    'Narva haigla',
    'Pärnu haigla',
    'Haapsalu haigla',
    'Järvamaa haigla (Paide)',
    'Rakvere haigla, Tapa haigла',
    'Valga haigла',
    'Viljandi haigла',
    'Lõuna-Eesti haigла (Võru), Põlва haigла'
]

# Функции
def validate_id(IDkoodtest, year, month, day):
    KontrollSumTest = 0
    if len(IDkoodtest) == 11 and IDkoodtest[0] in FirstNumber:
        NumbersTesty = int(IDkoodtest[1:3])
        if (0 <= NumbersTesty <= year) or (0 <= NumbersTesty < 100 and IDkoodtest[0] in FirstNumbertest):
            NumbersTestM = int(IDkoodtest[3:5])
            if (NumbersTesty == year and NumbersTestM <= month) or (1 <= NumbersTestM < 13):
                NumbersTest = int(IDkoodtest[5:7])
                if (NumbersTesty == year and NumbersTest == month and NumbersTest <= day) or (1 <= NumbersTest < 32):
                    return True
    return False

def calculate_control_sum(IDkoodtest):
    KontrollSumTest = 0
    lastnumberID = int(IDkoodtest[10])
    if lastnumberID != 0:
        for x in range(10):
            KontrollSumTest += int(IDkoodtest[x - 1]) * x
    else:
        for x in range(8):
            KontrollSumTest += int(IDkoodtest[x - 1]) * (x + 2)
        for x in range(4):
            KontrollSumTest += int(IDkoodtest[x + 6]) * x
    return KontrollSumTest

def determine_birthplace(birthplace):
    birthplace = int(birthplace)
    if 1 <= birthplace < 11:
        return Place[0]
    elif 11 <= birthplace < 21:
        return Place[1]
    elif 21 <= birthplace < 151:
        return Place[2]
    elif 151 <= birthplace < 161:
        return Place[3]
    elif 161 <= birthplace < 221:
        return Place[4]
    elif 221 <= birthplace < 271:
        return Place[5]
    elif 271 <= birthplace < 371:
        return Place[6]
    elif 371 <= birthplace < 421:
        return Place[7]
    elif 421 <= birthplace < 471:
        return Place[8]
    elif 491 <= birthplace < 521:
        return Place[9]
    elif 521 <= birthplace < 571:
        return Place[10]
    elif 571 <= birthplace < 601:
        return Place[11]
    elif 601 <= birthplace < 651:
        return Place[12]
    elif 651 <= birthplace < 701:
        return Place[13]
    else:
        return 'Error Birth Place'
