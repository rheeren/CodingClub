morsecode_conversion = {
  'A':'.-', 'B':'-...', 'C':'-.-.',
  'D':'-..', 'E':'.', 'F':'..-.',
  'G':'--.', 'H':'....', 'I':'..',
  'J':'.---', 'K':'-.-', 'L':'.-..',
  'M':'--', 'N':'-.', 'O':'---',
  'P':'.--.', 'Q':'--.-', 'R':'.-.',
  'S':'...', 'T':'-', 'U':'..-',
  'V':'...-', 'W':'.--', 'X':'-..-',
  'Y':'-.--', 'Z':'--..', '1':'.----',
  '2':'..---', '3':'...--', '4':'....-',
  '5':'.....', '6':'-....', '7':'--...',
  '8':'---..', '9':'----.', '0':'-----',
  '.':'.-.-.-', ',':'--..--', '?':'..--..',
  '!':'-.-.--', '"':'.-..-.', ':':'---...',
}

def encrypt(message):  
  phrase = ''
  for letter in message:
    if letter != ' ':
      phrase += morsecode_conversion[letter] + ' '
    else:
      phrase += ' '
  return phrase


message = input("Please type your message that you want to encrypt in Morse Code: ")
result = encrypt(message.upper())
print(result)
