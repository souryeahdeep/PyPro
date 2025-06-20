#Made this one learn the usage of functions and loops in Py

def acceptMessage(decision):
    message = input("Type your message: \n")
    shift = int(input("Type your shift number: \n"))
    caeser(message, shift, decision)


def caeser(message, shift, decision):
    output_text = ""
    for i in range(0, len(message)):
        var = message[i]
        if not var.isalpha():
            output_text += var
            continue
        j = ord(var)
        if decision == 'decode':
            j -= shift
            if j < 97:
                j += 26
        else:
            j += shift
            if j > 122:
                j -= 26
        output_text += chr(j)
    print(f"Here's your {decision}d message : {output_text}")
    
while True:
    choice = str(input("Type 'encode' to encrypt, and 'decode' to decrypt\n")).lower()
    acceptMessage(choice)
    if input("Type yes if you want to go again. Otherwise type no\n") == 'yes':
        continue
    else:
        break
