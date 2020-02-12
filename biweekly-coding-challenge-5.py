def encrypt(message):  
  message = message.split()
  a = 0
  b = 1
  newList = []
  for i in range(len(message)):
    if message[i][a] not in "aeiou":
      for j in range(len(message)):
        while message[i][b] not in "aeiou":
          b += 1
      newList.append(message[i][b:]+message[i][:b]+"ay")
      b = 1
    else:
      newList.append(message[i] + "yay")
  return ' '.join(newList)


message = input("Please type your message that you want to encrypt in Pig Latin: ")
result = encrypt(message.lower())
print(result)