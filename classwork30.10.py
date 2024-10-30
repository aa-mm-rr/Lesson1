class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. My age is {self.age}, and my gender is {self.gender}.")

class Member(Person):
    def __init__(self, name, age, gender, membership):
        super().__init__(name, age, gender)
        self.membership = membership

    def introduce(self):
        print(
            f"Hello, my name is {self.name}. My age is {self.age}, my gender is {self.gender}, and my membership is {self.membership}.")

class Author(Person):
    def __init__(self, name, age, gender, books_written):
        Person.__init__(self, name, age, gender)
        self.books_written = books_written

    def list_books(self):
        print(self.books_written)

class Authormember(Author, Member):
    def __init__(self, name, age, gender, membership, books_written):
        Member.__init__(self, name, age, gender, membership)
        Author.__init__(self, name, age, gender, books_written)

    def introduce(self):
        print(f"Hello, my name is {self.name}. I have written {self.books_written}.")
librarymembers = [
    Authormember("Karolia", 36, "f", "875.p", ["Sunny puppies"]),
    Authormember("Jessia", 20, "f", "691.a", ["How to bake a good cake"]),
    Authormember("Luis", 28, "m", "658.o", ["Cute kitties"])
]

for member in librarymembers:
    member.introduce()