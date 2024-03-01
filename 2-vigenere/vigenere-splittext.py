file_path = 'vigenere.txt'

with open(file_path, 'r') as file:
    file_content = file.read()

content = file_content.replace("\n", "")

texts = [""] * 12  # Inisialisasi untuk menyimpan 12 segment

# Melakukan split data
for i in range(len(content)):
    texts[i % 12] += content[i]

# Menyimpan masing-masing data ke segment berbeda
for i, text in enumerate(texts):
    segment_file_path = f'segment_{i+1}.txt'
    with open(segment_file_path, 'w') as file:
        file.write(text)
    print(f"Text saved to {segment_file_path}")