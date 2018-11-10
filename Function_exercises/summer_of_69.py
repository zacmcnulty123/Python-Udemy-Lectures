#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with 
# a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers
def summer_of_69(a):
    result = 0
    add = True
    for i in a:
        if i == 6:
            add = False
        elif add == True:
            result = result + i
        elif add == False and i == 9:
            add = True
    return result

print(summer_of_69([1,3,5]))
print(summer_of_69([4,5,6,7,8,9]))
print(summer_of_69([2,1,6,9,11]))