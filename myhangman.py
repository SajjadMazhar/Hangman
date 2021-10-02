
word = 'sajjad'
guessed = ''
while True:
    guess = input("enter guess: ")
    guessed += guess
    for char in word:
        if char in guessed:
            print(char, end='')

        else:
            print('_', end='')



