import random
# Each character has a set number. Must be a square (ex. 5x5 6x6 7x7)
polybius_square = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12,
                   "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23,
                   "x": 24, "y": 25, "z": 26, "0": 27, "1": 28, "2": 29, "3": 30, "4": 31, "5": 32, "6": 33, "7": 34,
                   "8": 35, "9": 36, " ": 37, "!": 38, "@": 39, "#": 40, "$": 41, "%": 42, "^": 43, "&": 44, "*": 45,
                   "(": 46, ")": 47, "?": 48, ":": 49}
reverse_square = [0] * 49
size_of_box = 7

used = [False] * 49

#Gives each letter a random value and makes sure there are no repeats
def shuffle():
    for key in polybius_square:
        rando = random.randint(0, 48)
        while used[rando]:
            rando = random.randint(0, 48)
        polybius_square[key] = rando + 1
        used[rando] = True

#Finds each letter's position in the square
def getIndex(index):
    row = int(index / size_of_box)
    column = index % size_of_box
    code = str(row) + str(column) + " "
    #Returns the place in the square
    return code

#Asks user to encrypt or decrypt
encrypt_or_decrypt = input("e for encrypt, d for decrypt: ")
#If there is an unknown input program prints error message
if encrypt_or_decrypt != "e" and encrypt_or_decrypt != "d":
    print("Invalid request!")
elif encrypt_or_decrypt == "e":
    message = input("Enter your message to encrypt: ").lower()

    newMessage = ""

    shuffle()
    #Saves the square for decryption later
    f = open("polybius_square.txt", "w")
    for key in polybius_square:
        #Writes file
       f.write(str(polybius_square[key]) + "_" + key + "\n")
    f.close()
    for i in range(0, len(message)):
        index = polybius_square[message[i]]
        newMessage += getIndex(index)
    #Prints encrypted message
    print(newMessage)
else:
    #Opens file and loads encrypted square for decryption
    f = open("polybius_square.txt")
    for line in f:
        keys = line.split("_")
        reverse_square[int(keys[0]) - 1] = keys[1].strip("\n")
    message = input("Enter message to decrypt: ")
    message = message.split(" ")
    print(message)
    newMessage = ""
    #Decrypts the message
    for code in message:
        index1 = int(code[0])
        index2 = int(code[1])
        newMessage += reverse_square[(index1 * size_of_box) + (index2 - 1)]
    print(newMessage)
