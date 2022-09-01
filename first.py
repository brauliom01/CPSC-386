def greet(name):
    print('Hi, ', name)

def sum(a, b, c):
    return a + b + c

def sumlist(li):
    total = 0
    for el in li:
        total += el
    return total

def sumany(*args):
    total = 0
    for el in args:
        total += el
    return total

def addany(*args):
    length = len(args)
    result = args [0]
    for i in range(1, length):
        result += args[i]
    return length

def main():
    #greet('Paul')
    li = ['Ralph', 'Lauren', 'Isaac']

    length = len(li)
    for i in range(length):
        greet(li[i])
    print(a)

    #print(sum[1,2,3])   # 3 things in the list, 0 in the dict
    #
    #print(sum[5,6, c=3]) # 2 things in the list 1 in the dict
