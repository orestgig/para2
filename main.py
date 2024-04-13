# class Student:
#     amount_of_students = 0
#     def __init__(self, height=0, name="noname", mark=0):
#         self.mark = mark
#         self.height = height
#         self.name = name
#         print("Зріст: ", self.name, ": ", self.height, self.mark)
#         Student.amount_of_students += 1
#
#     def growUp(self):
#         self.height += 10
#
#     def growmark(self):
#         self.mark += 1
#
# stepan = Student()
# maxym = Student(height=180, name="Максим", mark=12)
# kate = Student(height=170, name="Катя", mark=12)
# vlad = Student()
# print(Student.amount_of_students)
#
#
# print(maxym.height)
# maxym.growUp()
# print(maxym.height)
#
# print(maxym.mark)
# maxym.growmark()
# print(maxym.mark)



# print("Зріст Макса", maxym.height)
# print("Зріст Каті:", kate.height)
# print("Зріст Степана:", stepan.height)

class Student:
    def __init__(self, name="none"):
        self.name = name


    def __str__(self):
        return f"Hello, my name is {self.name}"

    def __del__(self):
        print("I'm graduater))))")

stud = Student("Andriy")
print(stud)
























































