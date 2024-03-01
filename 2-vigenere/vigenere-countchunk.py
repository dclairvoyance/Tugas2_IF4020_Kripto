chunksize = 9
file_path = 'vigenere.txt'

# Membaca dan melakukan sanitasi data dari file
with open(file_path, 'r') as file:
    file_content = file.read()

content = file_content.replace("\n", "")
chunks_arr = []

# Mencari setiap chunk yang berulang serta berapa kali chunk berulang
for i in range (0,len(content)-chunksize):
  chunk = content[i:i+chunksize]
  foundNumber = 0
  isFound = False
  for j in range (i+1,len(content)-chunksize):
    chunk_compare = content[j:j+chunksize]
    if(chunk == chunk_compare and chunk not in chunks_arr):
      foundNumber += 1
      isFound = True

      '''
      if(j-i <= 100):
        print(chunk_compare)
        print(str(j-i))
      '''
      
  if (isFound):
    chunks_arr.append(chunk)

  if foundNumber > 0:
    print(chunk)
    print(str(foundNumber))
    print("")
  

