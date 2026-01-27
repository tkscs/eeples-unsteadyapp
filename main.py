song = "I like to eat, eat, eat, apples and bananas"
typeOf = 3
def sing(vowel):
    if(typeOf == 1):
        print(song.replace("a",vowel))
    elif(typeOf == 2):
        newString = ""
        for i in song:
            if(i == "a"):
                newString += vowel
            else:
                newString += i
        print(newString)
    elif typeOf == 3:
        for i in song:
            print((i * (i!="a")) + ((vowel)* (i=="a")),end="")
        print("")
sing("ay")
sing("ee")
sing("i")
sing("o")
sing("u")
