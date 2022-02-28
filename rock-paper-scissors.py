import random

active = True

def run():
    def message():
        print(f"You choose {option_list[int(choose)-1]} and the computer choose {cpu_choose}")
    
    def win():
        print("You win")


    global active
    print("Welcome to the game: rock, scissors, paper, lizard and spock")
    option = input("Press 1 to start the game or 2 to exit ")
    while active == True:
        option_list = ["Rock", "Scissors", "Paper", "Lizard", "Spock"]
        cpu_choose = random.choice(option_list)
        if int(option) == 1:
            choose = input("""Choose an option of the list:
            1. Rock
            2. Scissors
            3. Paper
            4. Lizard
            5. Spock
            6. Exit
            """)

            # If user and computer choose the same option
            if option_list[int(choose)-1] == cpu_choose:
                print("It´s a draw")
                message()

            # If user choose Rock
            elif int(choose) == 1 and (cpu_choose == "Scissors" or cpu_choose == "Lizard"):
                win()
                message()
                print(f"{option_list[int(choose)-1]} crushes {cpu_choose}!")

            # If user choose Scissors
            elif int(choose) == 2 and (cpu_choose == "Lizard" or cpu_choose == "Paper"):
                win()
                message()
                if cpu_choose == "Lizard":  
                    print(f"{option_list[int(choose)-1]} decapitates {cpu_choose}!")
                else:
                    print(f"{option_list[int(choose)-1]} cut {cpu_choose}!")
            
             # If user choose Paper
            elif int(choose) == 3 and (cpu_choose == "Spock" or cpu_choose == "Rock"):
                win()
                message()
                if cpu_choose == "Spock":  
                    print(f"{option_list[int(choose)-1]} disproves {cpu_choose}!")
                else:
                    print(f"{option_list[int(choose)-1]} covers {cpu_choose}!")

             # If user choose Lizard
            elif int(choose) == 4 and (cpu_choose == "Spock" or cpu_choose == "Paper"):
                win()
                message()
                if cpu_choose == "Spock":  
                    print(f"{option_list[int(choose)-1]} poisons {cpu_choose}!")
                else:
                    print(f"{option_list[int(choose)-1]} eats {cpu_choose}!")

             # If user choose Spock
            elif int(choose) == 5 and (cpu_choose == "Scissors" or cpu_choose == "Rock"):
                win()
                message()
                if cpu_choose == "Rock":  
                    print(f"{option_list[int(choose)-1]} vaporizes {cpu_choose}!")
                else:
                    print(f"{option_list[int(choose)-1]} smashes {cpu_choose}!")
                
        elif int(option) == 2:
            active = False


if __name__ == "__main__":
    run()