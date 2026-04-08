from backend.dice import roll, get_face

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def take_turn(self):
        input(f"{self.name} → press Enter to roll...")
        result = roll()
        self.score += result
        print(f"You rolled: {result} {get_face(result)}")
        return result

class Computer:
    def __init__(self):
        self.name = "Computer"
        self.score = 0

    def take_turn(self):
        result = roll()
        self.score += result
        print(f"Computer rolled: {result} {get_face(result)}")
        return result