#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(a):
    boolList = [False, False]
    for i in a:
        if i == 0 and boolList[0] == False:
            boolList[0] = True
            continue
        elif i == 0 and boolList[1] == False:
            boolList[1] = True
            continue
        elif  boolList[0] == True and boolList[1] == True and i == 7:
            return True
        elif boolList[0] != True and i == 7:
            boolList[0] = False
            continue
    return False
    
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))