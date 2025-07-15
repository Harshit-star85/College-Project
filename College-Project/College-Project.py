class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | {status}"

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed = []

    def borrow_book(self, isbn):
        if isbn not in self.borrowed:
            self.borrowed.append(isbn)

    def return_book(self, isbn):
        if isbn in self.borrowed:
            self.borrowed.remove(isbn)

    def __str__(self):
        return f"{self.name} (ID: {self.user_id}) | Borrowed: {len(self.borrowed)} books"

class Library:
    def __init__(self):
        self.books = {}
        self.users = {}

    def add_book(self, title, author, isbn):
        if isbn in self.books:
            return False
        self.books[isbn] = Book(title, author, isbn)
        return True

    def register_user(self, name, user_id):
        if user_id in self.users:
            return False
        self.users[user_id] = User(name, user_id)
        return True

    def borrow_book(self, isbn, user_id):
        if isbn in self.books and user_id in self.users:
            book = self.books[isbn]
            user = self.users[user_id]
            if book.borrow():
                user.borrow_book(isbn)
                return True
        return False

    def return_book(self, isbn, user_id):
        if isbn in self.books and user_id in self.users:
            book = self.books[isbn]
            user = self.users[user_id]
            if isbn in user.borrowed and book.return_book():
                user.return_book(isbn)
                return True
        return False

    def search_books(self, query):
        result = []
        for book in self.books.values():
            if query.lower() in book.title.lower() or query.lower() in book.author.lower() or query in book.isbn:
                result.append(book)
        return result

    def show_books(self):
        for book in self.books.values():
            print(book)

    def show_users(self):
        for user in self.users.values():
            print(user)

    def user_books(self, user_id):
        if user_id in self.users:
            user = self.users[user_id]
            for isbn in user.borrowed:
                print(self.books[isbn])
        else:
            print("User not found")

def menu():
    lib = Library()
    while True:
        print("\n1.Add Book 2.Register User 3.Borrow 4.Return 5.Search 6.Show Books 7.Show Users 8.User's Books 0.Exit")
        ch = input("Choose: ")
        if ch == '1':
            t = input("Title: ")
            a = input("Author: ")
            i = input("ISBN: ")
            print("Added." if lib.add_book(t, a, i) else "Book exists.")
        elif ch == '2':
            n = input("Name: ")
            uid = input("User ID: ")
            print("Registered." if lib.register_user(n, uid) else "User exists.")
        elif ch == '3':
            i = input("ISBN: ")
            uid = input("User ID: ")
            print("Borrowed." if lib.borrow_book(i, uid) else "Failed.")
        elif ch == '4':
            i = input("ISBN: ")
            uid = input("User ID: ")
            print("Returned." if lib.return_book(i, uid) else "Failed.")
        elif ch == '5':
            q = input("Search: ")
            for b in lib.search_books(q):
                print(b)
        elif ch == '6':
            lib.show_books()
        elif ch == '7':
            lib.show_users()
        elif ch == '8':
            uid = input("User ID: ")
            lib.user_books(uid)
        elif ch == '0':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    menu()
