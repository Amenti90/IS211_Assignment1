def ListDivide(number=[], divide= 2):
    count= 0
    for i in number:
            if i % divide== 0:
                count = count +1
    return count

def ListException(x):
    print x

def testListDivide():
    if ListDivide([1,2,3,4,5])==2:
        print("ListDivide(1,2,3,4,5) works.")
    else:
        print ListException(x= "ListDivide(1,2,3,4,5) wont work.")
    if ListDivide([2,4,6,8,10]) == 5:
        print("ListDivide(2,4,6,8,10) works.")
    else:
        print ListException(x="ListDivide(2,4,6,8,10) wont work.")
    if ListDivide([30,54,63,98,100], divide=10) == 2:
        print("ListDivide(30,54,63,98,100) works.")
    else:
        print ListException(x="ListDivide(30,54,63,98,100) wont work.")
    if ListDivide([]) == 0:
        print("ListDivide() works.")
    else:
        print ListException(x="ListDivide() wont work.")
    if ListDivide([1, 2, 3, 4, 5], divide=1) == 5:
        print("ListDivide(1,2,3,4,5) works.")
    else:
        print ListException(x="ListDivide(1,2,3,4,5) wont work.")


testListDivide(),