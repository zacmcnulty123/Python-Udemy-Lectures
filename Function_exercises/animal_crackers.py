#ANIMAL CRACKERS: Write a function takes a two-word string and returns True
# If both words begin with same letter
def animal_crackers(text):
    split = text.split(" ")
    if split[0][0] == split[1][0]:
        return True
    else:
        return False

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
