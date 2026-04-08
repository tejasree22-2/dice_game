from backend.dice import roll, get_face

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def take_turn(self):
        result = roll()
        self.score += result
        print(f"{self.name} rolled: {result} {get_face(result)}")
        return result

class Computer(Player):
    def __init__(self):
        super().__init__("Computer")