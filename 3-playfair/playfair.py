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
    # bigram
    bigram_counter = Counter()
    bigrams = [ciphertext[index:index+2] for index in range (0, len(ciphertext) - 1, 2)]
    bigram_counter.update(Counter(bigrams))
    print("Bigrams: " + str(bigram_counter.most_common()) + "\n")

    # quadigram
    quadigram_counter = Counter()
    quadigrams = [ciphertext[index:index+4] for index in range (0, len(ciphertext) - 1, 4)]
    quadigram_counter.update(Counter(quadigrams))
    print("Quadigrams: " + str(quadigram_counter.most_common()) + "\n")

if __name__ == "__main__":
    ciphertext = load_ciphertext("3-playfair/playfair.txt")
    plaintext = ["_"*(len(ciphertext[0])-1)]*len(ciphertext)
    # frequency_table(ciphertext)
    for (line_index, line) in enumerate(ciphertext):
        for bigram_index in range (0, len(line), 2):
            if (ciphertext[line_index][bigram_index] == "H" and ciphertext[line_index][bigram_index+1] == "E"):
                plaintext[line_index] = plaintext[line_index][0:bigram_index] + "t" + plaintext[line_index][bigram_index+1:]
                plaintext[line_index] = plaintext[line_index][0:bigram_index+1] + "h" + plaintext[line_index][bigram_index+2:]
            elif (ciphertext[line_index][bigram_index] == "E" and ciphertext[line_index][bigram_index+1] == "L"):
                plaintext[line_index] = plaintext[line_index][0:bigram_index] + "h" + plaintext[line_index][bigram_index+1:]
                plaintext[line_index] = plaintext[line_index][0:bigram_index+1] + "e" + plaintext[line_index][bigram_index+2:]
            elif (ciphertext[line_index][bigram_index] == "Q" and ciphertext[line_index][bigram_index+1] == "X"):
                plaintext[line_index] = plaintext[line_index][0:bigram_index] + "i" + plaintext[line_index][bigram_index+1:]
                plaintext[line_index] = plaintext[line_index][0:bigram_index+1] + "n" + plaintext[line_index][bigram_index+2:]
            elif (ciphertext[line_index][bigram_index] == "M" and ciphertext[line_index][bigram_index+1] == "H"):
                plaintext[line_index] = plaintext[line_index][0:bigram_index] + "r" + plaintext[line_index][bigram_index+1:]
                plaintext[line_index] = plaintext[line_index][0:bigram_index+1] + "e" + plaintext[line_index][bigram_index+2:]
            elif (ciphertext[line_index][bigram_index] == "H" and ciphertext[line_index][bigram_index+1] == "M"):
                plaintext[line_index] = plaintext[line_index][0:bigram_index] + "e" + plaintext[line_index][bigram_index+1:]
                plaintext[line_index] = plaintext[line_index][0:bigram_index+1] + "r" + plaintext[line_index][bigram_index+2:]
            elif (ciphertext[line_index][bigram_index] == "A" and ciphertext[line_index][bigram_index+1] == "B"):
                plaintext[line_index] = plaintext[line_index][0:bigram_index] + "w" + plaintext[line_index][bigram_index+1:]
                plaintext[line_index] = plaintext[line_index][0:bigram_index+1] + "i" + plaintext[line_index][bigram_index+2:]
            elif (ciphertext[line_index][bigram_index] == "T" and ciphertext[line_index][bigram_index+1] == "H"):
                plaintext[line_index] = plaintext[line_index][0:bigram_index] + "a" + plaintext[line_index][bigram_index+1:]
                plaintext[line_index] = plaintext[line_index][0:bigram_index+1] + "t" + plaintext[line_index][bigram_index+2:]

        print(plaintext[line_index])
        print(ciphertext[line_index])
