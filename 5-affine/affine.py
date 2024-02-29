import math
import random

# Mencari modular multiplicative inverse
def mod_inv(left_var, right_var, n):
  for i in range (1,n):
    if left_var == (right_var * i) % n:
      return i

# Mencari nilai b dengan melakukan substitusi nilai m
# Serta nilai huruf plaintext dan ciphertext pertama
def final_substitution(a, c, m, n):
  for i in range (1,n):
    if a == (m * c + i) % n:
      return i

# Mencari nilai m dan b
def find_key(hex_values, n):
  byte_values = [0xFF, 0xD8, 0xFF, 0xE0]
  left_var = int(hex_values[1], 16) - int(hex_values[0], 16)
  right_var = int(byte_values[1]) - int(byte_values[0])

  if left_var<0:
    left_var += n
  
  # if right_var<0:
  #   right_var += n

  m = mod_inv(left_var, right_var, n)
  b = final_substitution(int(hex_values[0], 16), int(byte_values[0]), m, n)

  return m,b

# Melakukan decipher dari ciphertext
def affine_decipher(hex_values, m, b, n):
  plain_hex = []
  m_inv = mod_inv(1,m,n)
  for i in range(len(hex_values)):
    C = hex((m_inv * (int(hex_values[i], 16) - b)) % n)
    plain_hex.append(C)
  return plain_hex

# Pembacaan dan penulisan file diambil dari source code penjelasan tugas Nomor 5
def read_image_to_hex(image_path):
  try:
    with open(image_path, "rb") as image:
      f = image.read()
      b = bytearray(f)
      array_of_hex = [hex(byte) for byte in b]
      return array_of_hex
  except FileNotFoundError:
    print("Error: File not found.")
    return None
  except ValueError as e:
    print("Error:", e)
    return None
  
def array_of_hex_to_bytearray(array_of_hex):
  bytearray_data = bytearray()
  for hex_value in array_of_hex:
    if hex_value.startswith('0x'):
      hex_value = hex_value[2:]
    byte_value = int(hex_value, 16)
    bytearray_data.append(byte_value)
  return bytearray_data

def create_file_from_bytes(file_path, bytes_data):
  try:
    with open(file_path, "wb") as file:
      file.write(bytes_data)
    print("File berhasil dibuat:", file_path)
  except Exception as e:
    print("Error:", e)
  
def main():
  image_path = "./chall.jpg"
  n = 256
  hex_values = read_image_to_hex(image_path)

  if hex_values is not None:
    m,b = find_key(hex_values, n)
    print("hasil m adalah: " + str(m))
    print("hasil b adalah: " + str(b))
    cipher_hex = affine_decipher(hex_values, m, b, n)
    bytearray_cipher = array_of_hex_to_bytearray(cipher_hex)
    create_file_from_bytes("./chall_decrypt.jpg", bytearray_cipher)

if __name__ == "__main__":
  main()

