from collections import Counter

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Error reading file: {e}"

def frequency_table(ciphertext):
    # letter
    letter_counter = Counter()
    letters =  [letter for letter in ciphertext]
    letter_counter.update(Counter(letters))
    print("Letters: " + str(letter_counter.most_common()) + "\n")

if __name__ == "__main__":
    ciphertext = read_file("2-vigenere/segment_1.txt")
    frequency_table(ciphertext)