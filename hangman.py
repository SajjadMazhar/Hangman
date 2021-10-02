from random import choice

words = [
    "computer", "elephant", "piano", "sparrow", "physics"
]
hints = [
    "electronic device", "animal", "music", "bird", "science"
]

word = choice(words)
hint = hints[words.index(word)]
word_list = [x for x in word]
word_size = len(word)
guessed_text = '_'*word_size
guessed = False
counter = 0
lives = 8

cheer_up = ["NICE..!", "COOL..!!", "RIGHT..", "CORRECT..!!!"]
cheer_down = ["What are you doing?? ", "Wrong one!! keep Trying.", "I can't believe that.", "ok, let's try again.."]

print(f"***{guessed_text}***")
print(f"HINT: {hint}")

# calculating percentage and per20
def calc_percent_bar(word_count, total_count):
    ratio = word_count/total_count
    per20 = ratio * 20
    percent = per20 * 5
    return [per20, percent]

# loop will not end untill guessed = True or the game overs
while not guessed:
    
    inputGuess = input("Guess The Letter: ").lower()

    # checking whether the input is there in word or not
    if inputGuess in word:

        # looping through each character one by one of the given word and compare it with input character
        for char in word:
            if inputGuess == char:
                if inputGuess in word_list:
                    char_index = word_list.index(char)
                    word_list[char_index] = '_'
                    guessed_text = "".join((guessed_text[:char_index], inputGuess, guessed_text[char_index+1:]))
                    counter+=1 # counter increases by 1 each time the input character matches with the character in word
        print(f"\n{choice(cheer_up)}")
    else:
        lives-=1
        if lives == 0:
            print("Oops.. You failed.. Game Over!")
            break
        print(f"{choice(cheer_down)} You have {lives} live(s) left.")
    
    # comparing counter with length of word to confirm winning condition
    if counter == word_size:
        guessed = True
        print("Well Done..! You Win.")
    
    # creating percent progress bar 
    percent_bar = "#"*round(calc_percent_bar(counter, word_size)[0])
    print(f"Your progress... {percent_bar} {round(calc_percent_bar(counter, word_size)[1], 1)}% solved.")
    print(f"\n***{guessed_text}***\n")


