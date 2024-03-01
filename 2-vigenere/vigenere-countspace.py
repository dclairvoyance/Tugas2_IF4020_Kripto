file_path = 'vigenere.txt'
text = "WUMJRBAUL"
chunksize = len(text)

# Membaca dan melakukan sanitasi data dari file
with open(file_path, 'r') as file:
    file_content = file.read()

content = file_content.replace("\n", "")
a = 0

space_arr = []
# Mencari jarak antara input text
for i in range (0, len(content)-chunksize):
  chunk = content[i:i+chunksize]
  if (chunk == text):
    b = i-a
    space_arr.append(b)
    a = i

print(space_arr[1:len(space_arr)])

