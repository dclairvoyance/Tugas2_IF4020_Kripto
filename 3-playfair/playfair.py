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

def check_bigram_ciphertext(bigram, ciphertext, line_index, bigram_index):
    return ciphertext[line_index][bigram_index] == bigram[0] and ciphertext[line_index][bigram_index+1] == bigram[1]

def replace_bigram_plaintext(bigram, plaintext, line_index, bigram_index):
    plaintext[line_index] = plaintext[line_index][0:bigram_index] + bigram[0] + plaintext[line_index][bigram_index+1:]
    plaintext[line_index] = plaintext[line_index][0:bigram_index+1] + bigram[1] + plaintext[line_index][bigram_index+2:]

if __name__ == "__main__":
    ciphertext = load_ciphertext("3-playfair/playfair.txt")
    plaintext = ["_"*(len(ciphertext[0])-1)]*len(ciphertext)
    # frequency_table(ciphertext)
    for (line_index, line) in enumerate(ciphertext):
        for bigram_index in range (0, len(line), 2):
            if (check_bigram_ciphertext("HE", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("th", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("EH", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("ht", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("EL", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("he", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("LE", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("eh", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("QX", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("in", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("XQ", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("ni", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("MH", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("re", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("HM", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("er", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("TH", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("at", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("HT", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("ta", plaintext, line_index, bigram_index)

            # ekspansi Playfair square
            elif (check_bigram_ciphertext("HL", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("te", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("LH", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("et", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("HA", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("tl", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("AH", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("lt", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("EA", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("hl", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("AE", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("lh", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("ET", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("ha", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("TE", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("ah", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("LA", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("el", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("AL", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("le", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("LT", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("ea", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("TL", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("ae", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("TA", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("al", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("AT", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("la", plaintext, line_index, bigram_index)

            elif (check_bigram_ciphertext("KH", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("yw", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("HK", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("wy", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("CA", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("gt", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("AC", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("tg", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("EX", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("an", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("XE", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("na", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("TM", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("ev", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("MT", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("ve", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("HY", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("wh", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("YH", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("hw", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("AF", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("lx", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("FA", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("xl", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("SX", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("gs", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("XS", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("sg", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("WK", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("ry", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("KW", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("yr", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("HQ", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("ey", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("QH", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("ye", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("NH", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("we", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("HN", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("ew", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("DW", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("kn", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("WD", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("nd", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("HF", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("lt", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("FH", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("tl", plaintext, line_index, bigram_index) 
            elif (check_bigram_ciphertext("LD", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("eo", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("DL", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("oe", plaintext, line_index, bigram_index) 
            elif (check_bigram_ciphertext("BL", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("ft", plaintext, line_index, bigram_index)
            elif (check_bigram_ciphertext("LB", ciphertext, line_index, bigram_index)):
                replace_bigram_plaintext("tf", plaintext, line_index, bigram_index) 
            
            # ekspansi Playfair square
            # elif (check_bigram_ciphertext("KD", ciphertext, line_index, bigram_index)):
            #     replace_bigram_plaintext("ck", plaintext, line_index, bigram_index)
            # elif (check_bigram_ciphertext("DK", ciphertext, line_index, bigram_index)):
            #     replace_bigram_plaintext("kc", plaintext, line_index, bigram_index) 
            # elif (check_bigram_ciphertext("KO", ciphertext, line_index, bigram_index)):
            #     replace_bigram_plaintext("cd", plaintext, line_index, bigram_index)
            # elif (check_bigram_ciphertext("OK", ciphertext, line_index, bigram_index)):
            #     replace_bigram_plaintext("dc", plaintext, line_index, bigram_index)
            # elif (check_bigram_ciphertext("KG", ciphertext, line_index, bigram_index)):
            #     replace_bigram_plaintext("co", plaintext, line_index, bigram_index)
            # elif (check_bigram_ciphertext("GK", ciphertext, line_index, bigram_index)):
            #     replace_bigram_plaintext("oc", plaintext, line_index, bigram_index)  
            # elif (check_bigram_ciphertext("KC", ciphertext, line_index, bigram_index)):
            #     replace_bigram_plaintext("cg", plaintext, line_index, bigram_index)
            # elif (check_bigram_ciphertext("CK", ciphertext, line_index, bigram_index)):
            #     replace_bigram_plaintext("gc", plaintext, line_index, bigram_index) 
            # elif (check_bigram_ciphertext("DO", ciphertext, line_index, bigram_index)):
            #     replace_bigram_plaintext("kd", plaintext, line_index, bigram_index)
            # elif (check_bigram_ciphertext("OD", ciphertext, line_index, bigram_index)):
            #     replace_bigram_plaintext("dk", plaintext, line_index, bigram_index) 
            # elif (check_bigram_ciphertext("DG", ciphertext, line_index, bigram_index)):
            #     replace_bigram_plaintext("ko", plaintext, line_index, bigram_index)
            # elif (check_bigram_ciphertext("GD", ciphertext, line_index, bigram_index)):
            #     replace_bigram_plaintext("ok", plaintext, line_index, bigram_index) 
            # elif (check_bigram_ciphertext("DC", ciphertext, line_index, bigram_index)):
            #     replace_bigram_plaintext("kg", plaintext, line_index, bigram_index)
            # elif (check_bigram_ciphertext("CD", ciphertext, line_index, bigram_index)):
            #     replace_bigram_plaintext("gk", plaintext, line_index, bigram_index) 
            # elif (check_bigram_ciphertext("OG", ciphertext, line_index, bigram_index)):
            #     replace_bigram_plaintext("do", plaintext, line_index, bigram_index)
            # elif (check_bigram_ciphertext("GO", ciphertext, line_index, bigram_index)):
            #     replace_bigram_plaintext("od", plaintext, line_index, bigram_index) 
            # elif (check_bigram_ciphertext("OC", ciphertext, line_index, bigram_index)):
            #     replace_bigram_plaintext("dg", plaintext, line_index, bigram_index)
            # elif (check_bigram_ciphertext("CO", ciphertext, line_index, bigram_index)):
            #     replace_bigram_plaintext("gd", plaintext, line_index, bigram_index) 
            # elif (check_bigram_ciphertext("GC", ciphertext, line_index, bigram_index)):
            #     replace_bigram_plaintext("og", plaintext, line_index, bigram_index)
            # elif (check_bigram_ciphertext("CG", ciphertext, line_index, bigram_index)):
            #     replace_bigram_plaintext("go", plaintext, line_index, bigram_index) 

        print(plaintext[line_index])
        print(ciphertext[line_index])
