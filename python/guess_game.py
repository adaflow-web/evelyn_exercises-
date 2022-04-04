def guess_game(): 
    number = 5
    color = "green"
    user_number = int(input("Enter a number from 1 to 20: "))
    user_color = input("Enter a color: ") 
    if user_number == number and user_color == color:
        print("CONGRATULATIONS!")
        print ("You have solved the misteries")
    elif user_number == number or user_color == color:
        print("Not bad")
        print ("You have solved at least one of the misteries")
    else:
       print("Not even close!")
       print("Game Over!")

    print("Let's keep playing") 


guess_game()
guess_game()
guess_game()