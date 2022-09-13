class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def eat(self):
        print(f"{self.name} is eating food.")


class Student(People):
    def __init__(self, name, age, student_id):
        People.__init__(self, name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studing.")

    # 覆寫parent class的method 注意要提供需要的parameter
    # 若沒有提供會有錯誤，那要如何呼叫parent class原來的method呢?
    def eat(self, food):
        # super().eat()
        print(f"{self.name} is now eating {food}.")
        # 不自覺寫成self.food


student_one = Student("Wilson", 25, 100)
print(student_one.name)
print(student_one.age)
student_one.sleep()
student_one.study()
student_one.eat("beef")
p = People("Wilson", 25)
p.eat()
