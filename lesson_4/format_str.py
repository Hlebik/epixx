# format_str.py
def f1(var1, var2):
    return var1 + ' � ' + var2

def f2(var1, var2):
    return '{0} � {1}'.format(var1, var2)

def f3(var1, var2):
    return f'{var1} � {var2}'

print(f1('����', '���'))
print(f2('����', '���'))
print(f3('����', '���'))