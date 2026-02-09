def show_welcome():
    print("------------- WELCOME -------------")
    print("*" * 35)



def calculate_ave_score():
    player_name = input("Enter Player Name: ")
    game_played = int(input("Enter Number of Games Played: "))
    total_score = int(input("Enter Total Score: "))
    ave_score = total_score / game_played

    print(f"\nPlayer: {player_name}")
    print(f"Games Played: {game_played}")
    print(f"Total Score: {total_score}")
    print(f"Average Score: {ave_score:.2f}")
    print("*" * 35)
    print("Thanks for playing!")
    print("-" * 35)
    
show_welcome()
calculate_ave_score()
