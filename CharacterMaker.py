def(characterNameDefalut[i], characterName[i], characterCode[i]):
    print(characterCode[i]+"의 이름을 골라주세요: 1"+characterNameDefalut[i]+", 2 스스로 입력")
    characterNameSelect = input()
    endOfWhile = True
    while endOfWhile:
        if(characterNameSelect == "1"):
            print(characterNameDefalut[i]+"라는 이름으로 괜찮습니까? y/n")
            answerYesOrNo = input()
            if(answerYesOrNo == "y" or "Y" or "yes" or "Yes"):
                print("정말 훌륭한 이름이네요. "+characterCode[i]+"다워요")
                characterName[i] = characterNameDefalut
                endOfWhile = False
            else if(answerYesOrNo == "n" or "N" or "no" or "No"):
        else if(characterNameSelect == "2"):
            print("..이름을 입력하세요.")
            characterName[0] = input()


