from aquarium.fish import Fish


class Clownfish(Fish):

    def __init__(self, name, weight, color, stripe_color):
        Fish.__init__(self)
        self.name = name
        self.weight = weight
        self.color = color
        self.stripe_color = stripe_color

    # overriden method from fish class, stripe color is printed too
    def status(self):
        print(
            str(self.name) + ", weight: " + str(self.weight) + ", color: " + str(self.color) + ", stripe color: " + str(
                self.stripe_color))
