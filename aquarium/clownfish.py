from aquarium.fish import Fish

class Clownfish(Fish):

    def __init__(self, stripe_colour):
        Fish.__init__(self)
        self.stripe_colour = stripe_colour

    def feed(self):
        self.weight += 1

