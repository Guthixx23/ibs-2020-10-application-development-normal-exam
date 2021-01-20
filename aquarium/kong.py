from aquarium.fish import Fish

class Kong(Fish):

    def __init__(self):
        Fish.__init__(self)

    def feed(self):
        self.weight += 2