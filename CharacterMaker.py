from CharacterCode import defalutCharcterCode

characterCode = defalutCharcterCode()
characterName = [len(characterCode)]
characterNameDefalut = [len(characterCode)]

for i in characterCode.keys():
    characterNameDefalut[i] = characterCode[i].values()
    characterName[i] = characterNameDefalut[i]


def(characterCode[x]):
    print(characterCode[i].keys()+"의 이름을 골라주세요: 1"+characterNameDefalut[i]+", 2 스스로 입력")
    characterNameSelect = input()
    endOfWhile = True
    while endOfWhile:
        if(characterNameSelect == "1"):
            print(characterNameDefalut[i]+"라는 이름으로 괜찮습니까? y/n")
            answerYesOrNo = input()
            if(answerYesOrNo == "y" or "Y" or "yes" or "Yes"):
                print("정말 훌륭한 이름이네요. "+characterCode[i]+"다워요")
                characterName[i] = characterNameDefalut[i]
                characterCode[i] = characterNameDefalut[i]
                endOfWhile = False
            else if(answerYesOrNo == "n" or "N" or "no" or "No"):
                print("다시 선택해 주세요.")
                break
            else:
                print("y/n으로 입력해 주세요.")
                break
        else if(characterNameSelect == "2"):
            print("..이름을 입력하세요.")
            characterName[i] = input()
            print(characterName[i]+"라는 이름으로 괜찮습니까? y/n")
            answerYesOrNo = input()
            if(answerYesOrNo == "y" or "Y" or "yes" or "Yes"):
                print("정말 훌륭한 이름이네요. "+characterCode[i]+"다워요")
                characterCode[i] = characterName[i]
                endOfWhile = False
            else if(answerYesOrNo == "n" or "N" or "no" or "No"):
                print("다시 선택해 주세요.")
                break
            else:
                print("y/n으로 입력해 주세요.")
                break
        else:
            print("이름을"+characterNameSelect+"로 할까요? y/n")
            answerYesOrNo = input()
            if(answerYesOrNo == "y" or "Y" or "yes" or "Yes"):
                print("정말 훌륭한 이름이네요. "+characterCode[i]+"다워요")
                characterCode[i] = characterNameSelect
                endOfWhile = False
            else if(answerYesOrNo == "n" or "N" or "no" or "No"):
                print("다시 선택해 주세요.")
                break
            else:
                print("y/n으로 입력해 주세요.")
                break

