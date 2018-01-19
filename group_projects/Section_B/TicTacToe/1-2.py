#--------  *    ------      ---------     /\       ------       ---------   ------    ------
#   |      |   |                |        /  \     |                 |      |      |   |
#   |      |   |        ---     |       /    \    |        ---      |      |      |    -----
#   |      |   |                |      /------\   |                 |      |      |   |
#   |      |    ------          |     /        \   ------           |       ------    ------

print("Hello, my friend")
name=raw_input("What is your name? -- ")
age=int(raw_input("How old are you? -- "))
if age>=6:
    play=raw_input("Do u wanna play Tic-Tac-Toe? -- ")
    lower_play = play.lower()
    if play=="no":
        print("for what u come there")
    elif play=="yes":
        print("Nice!")
        rules=raw_input("do u know the rules of Tic-Tac-Toe? -- ")
        if rules=="No" or rules=="no":
            print("...") # write rules there
        else:
            print("Great!")
        print("So, let's Start")

else:
    print("This game is for 6 years and older guys")
    
