# ユーザーに年齢を尋ね、入力を年齢順に格納する
while True:
    print('Enter your age:')
    age = input()

    # 入力(age) が数字であれば現在のループから抜け出し、2番目のループに移動する。数字でない場合は再び入力を促す。
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

# ユーザーにパスワード(英数字のみ) を入力させる
while True:
    print('Select a new password (letters and numbers only):')
    password = input()

    # 入力(password) が英数字であればループから抜ける。英数字出ない場合はふたたび入力を促す。
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')
