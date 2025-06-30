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


print("--------------------------------------------------------------------------")
lib = Library("Центральная библиотека", "ул. Ленина, 10", [])
b1 = Book("Война и мир", "Л. Толстой", 1869)
b2 = Book("Мастер и Маргарита", "М. Булгаков", 1967)
lib.addBook(b1)
lib.addBook(b2)
print(b1.getInfo())
print(lib.listBooks())


# Task 2
class Student:

    def __init__(self, name: str, id: int, grades: list[int]):
        self.__name = name
        self.__id = id
        self.__grades = grades

    def get_id(self):
        return self.__id

    def get_profile(self) -> str:
        return f"Студент: {self.__name}, ID: {self.__id}"

    def assign_grade(self, grade: int) -> None:
        self.__grades.append(grade)


class Faculty:

    def __init__(self, name: str, students: list[Student]):
        self.__name = name
        self.__students = students

    def get_name(self):
        return self.__name

    def enroll(self, student: Student) -> None:
        if student not in self.__students:
            self.__students.append(student)
        else:
            print("Студент уже на факультете.")

    def graduate(self, student: Student) -> None:
        if student in self.__students:
            self.__students.remove(student)
        else:
            print("Студента нет на факультете.")

    def list_students(self):
        result = [stud.get_profile() for stud in self.__students]
        return result

    def find_student(self, id: str) -> Student | None:
        for stud in self.__students:
            if stud.get_id() == id:
                return stud


class University:

    def __init__(self, name: str, faculties: list[Faculty]):
        self.__name = name
        self.__faculties = faculties

    def add_faculty(self, f: Faculty) -> None:
        if f not in self.__faculties:
            self.__faculties.append(f)
        else:
            print("Факультет уже есть в списке университета.")

    def remove_faculty(self, f: Faculty) -> None:
        if f in self.__faculties:
            self.__faculties.remove(f)
        else:
            print("Такого фалькультета нет в списке университета.")

    def list_faculties(self):
        return [fac.get_name() for fac in self.__faculties]

    def find_faculty(self, name: str) -> Faculty | None:
        for _ in self.__faculties:
            if _.get_name() == name:
                return _

print("--------------------------------------------------------------------------")
uni = University("МГУ", [])
math = Faculty("Математический факультет", [])
ivan = Student("Иван Иванов", 12345, [])
uni.add_faculty(math)
math.enroll(ivan)
print(uni.list_faculties()) # ['Математический факультет']
print(math.list_students()) # ['Иван Иванов (12345)']
profile = ivan.get_profile()
print(profile) # Студент: Иван Иванов, ID: 12345