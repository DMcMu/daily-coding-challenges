#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#Follow-up: what if you can't use division?


#Use O(n) runtime and only one return array
def withDiv(a):
    if a == None or len(a) == 0:
        return []
    zero = False
    twoZero = False
    tot = 1
    for i in range(len(a)):
        if a[i] == 0 and zero == False:
            zero = True
        elif a[i] == 0 and zero == True:
            twoZero = True
            tot *= a[i]
        else:
            tot *= a[i]
    newA = [0] * len(a)
    for i in range(len(a)):
        if a[i] == 0 and twoZero == False:
            newA[i] == tot
        elif twoZero == False and zero == False:
            newA[i] = tot / a[i]

    return newA



#No division to use O(n) runtime and only one return array
def noDiv(a):
    newA = []
    right, left = 1, 1
    for num in reversed(a):
        newA.insert(0, right)
        right *= num
    for i in range(len(a)):
        newA[i] *= left
        left *= a[i]
    
    return newA
