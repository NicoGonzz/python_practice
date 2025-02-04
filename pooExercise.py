class Book:
    def __init__(self,title,author):
        self.title = title,
        self.author = author,
        self.available = True,
        pass

    def borrow(self):
        if self.available:
            self.available = False
            print(f"El {self.title} ha sido prestado")
        else:
            print(f"El libro no esta disponible")
        
    def return_book(self):
        self.available = True
        print(f"El libro {self.title} ha sido regresado")

class User:
    def __init__(self,name,user_id):
        self.name = name,
        self.user_id = user_id,
        self.borrowed_books = []
        pass

    def borrow_book(self,book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro {self.name} no esta disponible en el momento")
        
    def return_book(self,book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else: 
            print(f"El libro {book.title} no puede ser devuelto, ya que no esta en la clase prestada")

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        pass

    def add_books(self,book):
        self.books.append(book)
        print(f"El libro {book.title} ha sido agregado")

    def register_user(self,user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido agregado")

    def show_avaible_books(self):
        print("Libros disponibles: ")
        for book in self.books:
            if book.available:
                print(f"El libro {book.title} por {book.author} esta disponible")

#Books
book1 = Book('Don quijote de la mancha','Miguel Cervantes')
book2 = Book('Principito','Antoine de Saint')
book3 = Book('100 años de soledad','Gabriel Garcia Marquez')
book4 = Book('El Hobbit','Tolkien')

#Users
user1 = User('Juan Nicolas',1)
user2 = User('Natalia Contreras',2) 

#Library
library = Library()
library.add_books(book1)
library.add_books(book2)
library.add_books(book3)
library.add_books(book4)
library.register_user(user1)
library.register_user(user2)

#Show books
library.show_avaible_books()

#Lends
user1.borrow_book(book2)
user2.borrow_book(book4)
library.show_avaible_books()

#Return
user2.return_book(book4)
library.show_avaible_books()

user2.return_book(book3)