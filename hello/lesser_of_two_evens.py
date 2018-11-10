#LESSER IF TWO EVENS: Write a function that returns the lesser of two given numbers
# if both are even, but returns the greater is one or both numbers are odd
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return b
        else:
            return a
    else:
        if a > b:
            return a
        else:
            return b

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))