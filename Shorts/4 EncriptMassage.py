inputText = "c0ggj Ion D6gg0"
key = 5
mode = "lock"
# mode = "Unlock"
Output = ""

characters = 'abcdefghijklmnopqrstuvwxyz1234567890'
for char in inputText:
    if char  in characters:
        charIndex = characters.index(char)
        if mode == "lock":
            newCharIndex = (charIndex + key) % len(characters)
        elif mode == "Unlock":
            newCharIndex = (charIndex - key) % len(characters)
        Output += characters[newCharIndex]
    else:
        Output += char
print(Output)

