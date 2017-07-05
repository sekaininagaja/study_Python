# 「birthdays」辞書を定義
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    # 入力された値(名前)が「birthdays」辞書にある場合、「birthdays[name]」で誕生日を表示。
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)

    # 入力された値(名前)が「birthdays」辞書にない場合、誕生日を入力させて「birthdays」辞書を更新する。
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
