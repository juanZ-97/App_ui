test = '(1,3)'
test1 = test.split(',')
test2 = test1[0].split('(')
test3 = test1[1].split(')')
x = int(((test.split(','))[0].split('('))[1])
y = int(((test.split(','))[1].split(')'))[0])
print(x, y)

