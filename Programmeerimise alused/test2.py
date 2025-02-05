        print(f"It's {sex} Date of Birthday {DateBirth} Place of Birth {birthplace}")
        arvud.sort()
        print('Not correct IDkodes', arvud)
        M, W = [], []
        quantityOfIDinList = len(ikoodid)
        for x in range(quantityOfIDinList):
            tempID = ikoodid[x]
            if tempID[0] in ['1', '3', '5']:
                M.append(tempID)
            elif tempID[0] in ['2', '4', '6']:
                W.append(tempID)
            print('Women ID kodes', W)
            print("Men ID kodes", M)