def spam():
    eggs = 'spam local'
    print(eggs)

def bacon():
    print(eggs)
    spam()
    print(eggs)

eggs = 'global'
bacon()
print('eggs')
