class Robot:
    """Robot doctring"""

    # initialize the object's attributes / properties
    def __init__(self, inputname, inputage):
        self.name = inputname
        self.age = inputage

    # behaviors
    def walk(self):
        print(f"robot_{self.name} is walking.")

    def sleep(self, hours):
        print(f"robot_{self.name} is going to sleep for {hours} hours.")

    def test_self():
        print("no_self_keyword")


my_robot_1 = Robot("Wilson", 25)
print(my_robot_1.name)
print(my_robot_1.age)
print(my_robot_1.__doc__)
my_robot_1.walk()
my_robot_1.sleep(3)
# my_robot_1.test_self()
