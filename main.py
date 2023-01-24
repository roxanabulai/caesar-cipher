alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  """Encrypt given text."""
  new_text = ''
  for letter in list(text):
    pos = alphabet.index(letter) + shift
    if pos > len(alphabet):
      pos = pos % 26
    new_text = new_text + (alphabet[pos])
  return new_text

def decrypt(text, shift):
  """Decrypt given text."""
  new_text = ''
  for letter in list(text):
    pos = alphabet.index(letter) - shift
    if pos > len(alphabet):
      pos = pos % 26
    new_text = new_text + (alphabet[pos])
  return new_text

def caesar_cipher(text, shift, direction):
  """Choose between 'encrypt'/'decrypt'."""
  if shift > len(alphabet):
    shift = shift % 26
  if direction == "encode":
    new_text = encrypt(text, shift)
    print(f"Encoded text: {new_text}")
  elif direction == "decode":
    new_text = decrypt(text, shift)
    print(f"Encoded text: {new_text}")

caesar_cipher(text, shift, direction)