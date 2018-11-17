class Book():
    def __init__(self, title, author, pages):
        
        self.title = title
        self.author = author
        self.pages = pages
    #This is a magic method for a printing to string    
    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book object has been deleted')

b = Book('Python rocks', 'Jose', 200)
print(b.__str__())
print(len(b))