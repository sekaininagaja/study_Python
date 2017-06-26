spam = ['apples', 'bananas', 'tofu', 'cats']

# リストの内容をカンマで区切って表示する。
# 最後のitemの前には「and」をつける
def comma(data):
  spam.append(data)
  for i in range(len(spam)):
    if i != len(spam) - 1:
      print(spam[i] + ', ', end='')
    else:
      print('and ' + spam[-1] + '.')

# おまけでデータを入力させるようにしてみた
print("imput data: ", end='')
comma(str(input()))

