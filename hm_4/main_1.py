# Task 1
class Book:

    title: str
    author: str
    year: int

    def __init__(self, title: str, author: str, year: int):

        if year < 0: raise ValueError("Год выпуска не может быть отрицательным.")

        self.__title = title
        self.__author = author
        self.__year = year
        self.__bookmark = None

    def getInfo(self):
        return f"{self.__title}, {self.__author}, {self.__year}"

    def bookmarkPage(self, page: int) -> None:
        if page < 0: print("Закладка не установлена.")
        else:
            self.__bookmark = page
            print("Закладка установлена.")

    def updateTitle(self, new_title: str) -> None:
        self.__title = new_title
        print("Название изменено.")


class Library:

    name: str
    address: str
    books: list[Book]

    def __init__(self, name: str, address: str, books: list[Book]):
        self.__name = name
        self.__address = address
        self.__books = books

    def addBook(self, book: Book) -> None:
        if book not in self.__books:
            self.__books.append(book)
        else:
            print("Книга уже есть в библиотеке.")

    def removeBook(self, book: Book) -> None:
        if book in self.__books:
            self.__books.remove(book)
        else:
            print("Такой книги нет в библиотеке.")

    def listBooks(self) -> list[str]:
        result = [book.getInfo() for book in self.__books]
        return result


lib = Library("Центральная библиотека", "ул. Ленина, 10", [])
b1 = Book("Война и мир", "Л. Толстой", 1869)
b2 = Book("Мастер и Маргарита", "М. Булгаков", 1967)
lib.addBook(b1)
lib.addBook(b2)
print(b1.getInfo())
print(lib.listBooks())