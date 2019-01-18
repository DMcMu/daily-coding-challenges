#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def solution(a, k):
    if a == None or len(a) == 0 or k == None:
        return False
    dictio = {}
    for item in a:
        compl = k - item
        dictio[item] = compl
        if compl in dictio:
            return True
    
    return False


#This runs in one pass, uses n space and n complexity
