import random

active = True

def run():
    global active
    print("Welcome to the game: rock, scissors, paper, lizard and spock")
    option = int(input("Press 1 to start the game or 2 to exit "))
    while active == True:
        option_list = ["Rock", "Scissors", "Paper", "Lizard", "Spock"]
        cpu_choose = random.choice(option_list)
        if option == 1:
            choose = int(input("""Choose an option of the list:
            1. Rock
            2. Scissors
            3. Paper
            4. Lizard
            5. Spock 
            """))
            if choose == 1 and cpu_choose == option_list[0] or choose == 2 and cpu_choose == option_list[1] or choose == 3 and cpu_choose == option_list[2] or choose == 4 and cpu_choose == option_list[3] or choose == 5 and cpu_choose == option_list[4]:
                print("It´s a draw")
                print(f"You choose {option_list[choose-1]} and the computer choose {cpu_choose}")
            elif choose == 1 and cpu_choose == 2:
                print("It´s a draw")
                print(f"You choose {option_list[choose-1]} and the computer choose {cpu_choose}")
        elif option == 2:
            active = False


if __name__ == "__main__":
    run()