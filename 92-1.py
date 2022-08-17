# 92-1.py
class Robot:
    ingredient = "metal"

    def __init__(self, inputname, inputage):
        self.name = inputname
        self.age = inputage
        # 缺點是對於每個robot object建立時都佔記憶體空間
        # self.ingredient = "metal"

    def greet(self):
        print(
            f"Hi,my name is {self.name}. I am made of {self.__class__.ingredient}.")

    @staticmethod
    def greet2():  # staticmethod不用self
        print("A robot says hi...")


my_robot_1 = Robot("Wilson", 25)


print(Robot.ingredient)      # classname.attribute 建議少用，不然改classname時要改很多地方
print(my_robot_1.ingredient)  # class attribute
print(my_robot_1.__class__.ingredient)
my_robot_1.greet()
my_robot_1.greet2()
