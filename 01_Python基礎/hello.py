# This program says hello and asks for my name.

print('Hello world!')

# 名前を入力させて、表示する
print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)

# 入力した文字列を表示する
print('The length of your name is:')
print(len(myName))

# 年齢を入力させて、年齢 + 1 の結果を表示する
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
