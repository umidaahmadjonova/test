matn=input("matn kiriting: ")
vowels=[]
consonant=[]
for letter in matn:
    if letter in "AEUIOaeiou" and letter.isalpha():
        vowels.append(letter)
    elif letter.isalpha():
      consonant.append(letter)
print(vowels)
print(consonant)
    