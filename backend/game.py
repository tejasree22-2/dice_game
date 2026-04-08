from backend.player import Player, Computer

def start_game():
    name = input("Your name: ")
    player = Player(name)
    computer = Computer()

    for i in range(1, 4):
        print(f"\n--- Round {i} ---")
        p = player.take_turn()
        c = computer.take_turn()

    print(f"\nFinal → {player.name}: {player.score} | Computer: {computer.score}")
    if player.score > computer.score:   print("You win!")
    elif player.score < computer.score: print("Computer wins!")
    else:                               print("Tie!")
if __name__ == "__main__":
    start_game()
