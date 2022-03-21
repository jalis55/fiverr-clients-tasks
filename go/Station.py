class Station:
    def __init__(self, name, p):
        self.name = name
        self.p = float(p)
        self.connections = []
        self.next = None

    def __str__(self):
        return self.name + " " + str(self.p)

    def reverse(self):
        return reversed(self.connections)
