import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return '1 desu'
    elif answerNumber == 2:
        return '2 desu'
    elif answerNumber == 3:
        return '3 desu'
    elif answerNumber == 4:
        return '4 desu'
    elif answerNumber == 5:
        return '5 desu'
    elif answerNumber == 6:
        return '6 desu'
    elif answerNumber == 7:
        return '7 desu'
    elif answerNumber == 8:
        return '8 desu'
    elif answerNumber == 9:
        return '9 desu'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

