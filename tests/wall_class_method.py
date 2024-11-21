class Wall:
    armor = 10
    height = 5

    def fortify(self):
        self.armor *= 2

wall_one = Wall()
wall_one.fortify()
print(wall_one.armor)