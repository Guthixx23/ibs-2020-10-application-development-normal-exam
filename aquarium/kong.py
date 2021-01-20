from aquarium.fish import Fish


class Kong(Fish):

    def __init__(self):
        Fish.__init__(self)

    def feed(self):
        self.weight += 2

    def status(self):
        print(str(self.name) + ", weight: " + str(self.weight) + " colour: " + str(self.color))
