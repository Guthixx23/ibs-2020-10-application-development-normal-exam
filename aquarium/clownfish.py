from aquarium.fish import Fish


class Clownfish(Fish):

    def __init__(self, stripe_color):
        Fish.__init__(self)
        self.stripe_color = stripe_color

    def feed(self):
        self.weight += 1

    def status(self):
        print(
            str(self.name) + ", weight: " + str(self.weight) + " colour: " + str(self.color) + " stripe color: " + str(
                self.stripe_color))
