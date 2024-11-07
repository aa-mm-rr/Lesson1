class Publication:
    def __init__(self, name):
        self.name = name
    def print_information(self):
        print(f'Publication name is {self.name}')

class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages
    def print_information(self):
        super().print_information()
        print(f'Author is {self.author}')
        print(f'Amount of pages is {self.pages}')
class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor
    def print_information(self):
        super().print_information()
        print(f'Chief editor is {self.chief_editor}')

donaldDuck = Magazine('Donald Duck', 'Aki Hyppa')
compartmentN6 = Book('Compartment No 6', 'Rosa Liksom', 192)

print('Magazine information')
donaldDuck.print_information()
print('Book information')
compartmentN6.print_information()

