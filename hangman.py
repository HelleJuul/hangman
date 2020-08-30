import random as rd

print("H A N G M A N")

running = True

while running == True:
    status = input('Type "play" to play the game, "exit" to quit: ')
    
    if status == "play":
        allowed_fails = 8
        fails = 0

        words =["python", "java", "kotlin", "javascript"]
        word = rd.choice(words)
        hint_as_list = ["-"]*len(word)
        guesses = []

        while fails < allowed_fails:
            hint = "".join(hint_as_list)
            print(f"\n{hint}")

            if hint == word:
                print("You guessed the word!")
                print("You survived!")
                break
            else:
                guess = input(f"Input a letter: ")

                if len(guess) != 1:
                    print("You should input a single letter")

                elif guess not in "abcdefghjiklmnopqrstuvwxyz":
                    print("It is not an ASCII lowercase letter")

                elif guess in guesses:
                    print("You already typed this letter")

                elif guess not in word:
                    print("No such letter in the word")
                    guesses.append(guess)
                    fails += 1
                
                else:
                    positions = []
                    for pos, char in enumerate(word):
                        if char == guess:
                            positions.append(pos)

                    for pos in positions:
                        hint_as_list[pos]=guess
                    
                    guesses.append(guess)

        else:
            print("You are hanged!")

    elif status == "exit":
        running = False


