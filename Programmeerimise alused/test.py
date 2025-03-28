Password='Test123456789'
ListOfSymbols = ['!','@','#','$','%','^','&','*','(',')','_','+','=','-']
if len(Password) > 10:
    UpCase, LwCase, SpSymbol = None, None, None
    for x in range(len(Password)):
        if Password[x].isupper():
            UpCase = True
        if Password[x].islower():
            LwCase = True
        if Password[x] in ListOfSymbols:
            SpSymbol = True
        if LwCase == True and UpCase == True and SpSymbol == True:
            pass