#OLD MACDONALD write a function that capitalizes the first and fourth letters of a name
def old_macdonald(text):
    text = text[0].upper() + text[1:3] + text[3].upper() + text[4:]
    return text

print(old_macdonald('macdonald'))