secret_word = "Python"
guess = ""
guess_count = 0
guess_limit = 4
out_of_guesses = False

while secret_word != guess and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter a guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print('You Lose, out of guesses. Try Again')
else:
    print('congratulations! you win.')