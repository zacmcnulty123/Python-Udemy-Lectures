#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21,
# return their sum. If ther sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if ther sum (even after adjustment) exceeds 21, return 'BUST'
def black_jack(a,b,c):
    l = [a,b,c]
    result = 0
    if l.__contains__(11):
        result = result - 10
    result = result + a + b + c
    if result <= 21:
        return result
    else:
        return 'BUST'

print(black_jack(5,6,7))
print(black_jack(9,9,9))
print(black_jack(9,9,11))