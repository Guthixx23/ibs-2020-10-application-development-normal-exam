# parent class for method templates
class Fish():

    def __init__(self):
        self.name = ""
        self.weight = 0
        self.color = ""

    def status(self):
        print(str(self.name) + ", weight: " + str(self.weight) + ", color: " + str(self.color))

    def feed(self):
        self.weight += 1
