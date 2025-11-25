def num_of_letters(text,letters):
    text=text.lower()
    letter_counts={letter: text.count(letter) for letter in letters}

    return letter_counts
