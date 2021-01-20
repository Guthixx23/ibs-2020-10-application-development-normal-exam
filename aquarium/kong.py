from aquarium.fish import Fish


class Kong(Fish):

    def __init__(self, name, weight, color):
        Fish.__init__(self)
        self.name = name
        self.weight = weight
        self.color = color

    # overriden method from fish class, the amount of weight gain is doubled
    def feed(self):
        self.weight += 2
