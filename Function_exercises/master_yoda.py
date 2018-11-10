#MASTER YODA Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    split = text.split(" ")
    result = ""
    for i in range(len(split)-1, -1 , -1):
        result = result + " " + split[i]
    return result

print(master_yoda('I am Home'))
print(master_yoda('We are Ready'))