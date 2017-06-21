def spam():
    global eggs
    eggs = 'spam' # これはグローバル変数

def bacon():
    eggs = 'bacon' # これはローカル変数

def hamu():
    print(eggs) # これはグローバル変数

eggs = 42 # これはグローバル変数
spam()
print(eggs)
