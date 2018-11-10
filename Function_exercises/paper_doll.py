#PAPER DOLL: Given a string, return a stirng where for every character in the original there are three characters
def paper_doll(text):
    result = ""
    for i in text:
        for j in range(3):
            result = result + i
    return result

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))