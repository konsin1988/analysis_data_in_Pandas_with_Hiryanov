class Dog:
    def __init__(self, angry, count):
        self.angry = angry
        self.count = count

    def say_wow(self):
        if self.angry:
            print(*['WOW'] * self.count, sep='-')
        else:
            print(*['wow'] * self.count, sep='-')
    
    def ping(self):
        self.angry = True
    
    def feed(self, food_count):
        if food_count > 10:
            self.angry = False

my_dog = Dog(False, 3)
my_dog.say_wow()
my_dog.feed(20)
my_dog.say_wow()
my_dog.ping()
my_dog.say_wow()