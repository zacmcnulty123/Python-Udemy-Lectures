#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(a):
    if abs(100 - a) <= 10:
        return True
    elif abs(200 - a) <= 10:
        return True
    else:
        return False
print(almost_there(105))
print(almost_there(205))
print(almost_there(1))
