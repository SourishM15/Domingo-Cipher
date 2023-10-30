"""
Domingo Cipher
By: Sourish Mukherji
Sourish: 64018011@ep-student.org
"""
encrypt = ""
Alpha = ['A', 'B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
rev = [None] * 26

print("Type a word!")
UI = input().upper()
UIcharArray = [char for char in UI]
s = len(UIcharArray)
for x in range(26):
  rev[x] = Alpha[25-x]
  #print(rev[x])
for i in range(s):
  for j in range(26):
    if UIcharArray[i] == Alpha[j]:
      encrypt += rev[j]
print(encrypt)
