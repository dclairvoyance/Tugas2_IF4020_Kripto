from collections import Counter

def load_ciphertext(file_name):
    # ciphertext = ""
    ciphertext = []

    with open(file_name) as file:
        for line in file:
            # ciphertext += line[:len(line)-1]
            ciphertext.append(line)

    return ciphertext

def frequency_table(ciphertext):
    # letter
    letter_counter = Counter()
    letters =  [letter for letter in ciphertext]
    letter_counter.update(Counter(letters))
    print("Letters: " + str(letter_counter.most_common()) + "\n")

    # bigram
    bigram_counter = Counter()
    bigrams = [ciphertext[index:index+2] for index in range (len(ciphertext) - 1)]
    bigram_counter.update(Counter(bigrams))
    print("Bigrams: " + str(bigram_counter.most_common()) + "\n")

    # trigram
    trigram_counter = Counter()
    trigrams = [ciphertext[index:index+3] for index in range (len(ciphertext) - 2)]
    trigram_counter.update(Counter(trigrams))
    print("Trigrams: " + str(trigram_counter.most_common()) + "\n")

if __name__ == "__main__":
    ciphertext = load_ciphertext("1-monoalphabetic/monoalphabetic.txt")
    # plaintext = "_"*len(ciphertext)
    plaintext = ["_"*(len(ciphertext[0])-1)]*len(ciphertext)
    
    # replace H to T
    # ciphertext.replace("H", "T")

    # replace Z to H
    # ciphertext.replace("Z", "H")

    # replace I to L
    # ciphertext.replace("I", "L")

    # replace N to F
    # ciphertext.replace("N", "F")

    # for (index, letter) in enumerate(ciphertext):
    #     if (letter == "E"):
    #         plaintext = plaintext[0:index] + "e" + plaintext[index+1:] 
    #     elif (letter == "H"):
    #         plaintext = plaintext[0:index] + "t" + plaintext[index+1:]
    #     elif (letter == "Z"):
    #         plaintext = plaintext[0:index] + "h" + plaintext[index+1:]

    for (line_index, line) in enumerate(ciphertext):
        for (letter_index, letter) in enumerate(line):
            if (letter == "E"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "e" + plaintext[line_index][letter_index+1:] 
            elif (letter == "H"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "t" + plaintext[line_index][letter_index+1:]
            elif (letter == "Z"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "h" + plaintext[line_index][letter_index+1:]
            elif (letter == "W"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "l" + plaintext[line_index][letter_index+1:]
            elif (letter == "B"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "r" + plaintext[line_index][letter_index+1:]
            elif (letter == "Y"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "a" + plaintext[line_index][letter_index+1:]
            elif (letter == "R"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "o" + plaintext[line_index][letter_index+1:]
            elif (letter == "O"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "g" + plaintext[line_index][letter_index+1:]
            elif (letter == "F"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "n" + plaintext[line_index][letter_index+1:]
            elif (letter == "X"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "c" + plaintext[line_index][letter_index+1:]
            elif (letter == "M"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "y" + plaintext[line_index][letter_index+1:]
            elif (letter == "V"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "p" + plaintext[line_index][letter_index+1:]
            elif (letter == "A"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "s" + plaintext[line_index][letter_index+1:]
            elif (letter == "L"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "i" + plaintext[line_index][letter_index+1:]
            elif (letter == "P"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "m" + plaintext[line_index][letter_index+1:]
            elif (letter == "C"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "d" + plaintext[line_index][letter_index+1:]
            elif (letter == "T"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "w" + plaintext[line_index][letter_index+1:]
            elif (letter == "G"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "f" + plaintext[line_index][letter_index+1:]
            elif (letter == "U"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "u" + plaintext[line_index][letter_index+1:]
            elif (letter == "I"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "k" + plaintext[line_index][letter_index+1:]
            elif (letter == "K"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "b" + plaintext[line_index][letter_index+1:]
            elif (letter == "D"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "x" + plaintext[line_index][letter_index+1:]
            elif (letter == "N"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "v" + plaintext[line_index][letter_index+1:]
            elif (letter == "Q"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "q" + plaintext[line_index][letter_index+1:]
            elif (letter == "J"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "j" + plaintext[line_index][letter_index+1:]
            elif (letter == "S"):
                plaintext[line_index] = plaintext[line_index][0:letter_index] + "z" + plaintext[line_index][letter_index+1:]
        
        print(plaintext[line_index])
        print(ciphertext[line_index])