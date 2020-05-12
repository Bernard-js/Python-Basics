def translation(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "K"
            else:
                translation = translation + "k"
        else:
            translation = translation + letter
    return translation


print(translation(input("Enter a phrase: ")))