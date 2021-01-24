alphabet = "abcdefghijklmnoprstuvwxyzabcdefghijklmnoprstuvwxyz"
text = input("Enter messange: ")
key = 4
text = text.lower()
password = ""
for i in text:
    a = alphabet.find(i)
    b = a + key
    if i in alphabet:
        password = password + alphabet[b]
else:
     password = password + i
     print("your : ", password)