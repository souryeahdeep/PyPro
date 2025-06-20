import AcceptMessage as mx

while True:
    choice = str(input("Type 'encode' to encrypt, and 'decode' to decrypt\n")).lower()
    mx.acceptMessage(choice)
    if input("Type yes if you want to go again. Otherwise type no\n") == 'yes':
        continue
    else:
        break

# 32,40,53,76,114,172
# 8,13,23,38,58
# 5,10,15,20
# 5
