#Write a function that computes the volume of a sphere
def calcVolume(radius):
    result = 4/3 * 3.14 * radius**3;
    return result
print(calcVolume(2))
#Write a function that checks whether a number is in a given range(inclusive of high and low)
def ran_check(num, low, high):
    if(range(low, high).__contains__(num)):
        return "{} is in the ranger between {} and {}".format(num,low,high)
print(ran_check(5,2,7))

#Write a python function that accepts a string and calculates the number of upper case letters and lower case letters
def up_low(text):
    up = 0 
    low = 0
    for i in text:
            if i.isupper():
                up += 1
            elif i.islower():
                low += 1
    return "No. of Upper case characters: {} \nNo. of Lower case characters: {}".format(up, low)
print(up_low("Hello Mr. Rogers, how are you this fine Tuesday?"))

#write a python function that takes a list and returns a new list with unique elements of the first list
def unique_list(lst):
    uni = []
    for i in lst:
        if uni.__contains__(i):
            continue
        else:
            uni.append(i)
    return uni
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

#Write a python function that checks whether a passed in string is palindrome or not
def palindrome(text):
    rev = ""
    for i in range(len(text)-1,-1, -1):
        rev = rev + text[i]
    if rev == text:
        return True
    else:
        return False
print(palindrome('helleh'))

#Write a python function to check whether a string is pangram or not
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    lst = list(alphabet)
    for i in str1:
        if not lst.__contains__(i):
            continue
        elif lst.__contains__(i):
            lst.remove(i)
    return not lst
    return False
print(ispangram('The quick brown fox jumps over the lazy dog'))