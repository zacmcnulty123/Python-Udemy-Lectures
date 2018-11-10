# PRINT BIG: Write a function that takes in a single letter, and returns a 5 x 5 representation of that letter
myDict = {
    "a": "   *\n  * *\n *****\n *   *\n *   *"
}

def print_big(letter):
    return myDict[letter.lower()]
print(print_big('a'))