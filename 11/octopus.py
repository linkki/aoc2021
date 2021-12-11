class Octopus:

    flashes = 0
    flashes_this_round = 0

    def __init__(self, energy: int, x, y):
        self.energy = energy
        self.flashed = False
        self.x = x
        self.y = y

    def increase_energy(self, octopuses: list):
        if not self.flashed:
            self.energy += 1
        if self.energy == 10:
            self.energy = 0
            self.flashed = True
            Octopus.flashes += 1
            Octopus.flashes_this_round += 1
            for i in [self.x -1, self.x, self.x +1]:
                for j in [self.y -1, self.y, self.y +1]:
                    if i>=0 and j>=0 and i<10 and j<10 and not (i==self.x and j==self.y):
                        octopuses[j][i].increase_energy(octopuses)

    def new_step(self):
        Octopus.flashes_this_round = 0
        self.flashed = False