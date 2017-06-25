# 引数を1つあたえる。
# 与えられた引数が奇数だったら「number // 2」する。
# 与えられた引数が偶数だったら「3 * number + 1」

def collatz():
    try:
        number = int(input())
        if number%2 == 1: #奇数
            result = number // 2
            print(result)
        elif number%2 == 0: #偶数
            result = 3 * number + 1
            print(result)
    except:
        print("数字を入力してください")

collatz()
