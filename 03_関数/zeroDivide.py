def spam(divideBy):
    return  42 / divideBy
    

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))  # ここで処理が止まる
    print(spam(1))  # これは実施されない
except ZeroDivisionError:
    print('Error: Invalid argument.')


