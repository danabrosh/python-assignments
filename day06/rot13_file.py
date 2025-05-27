filename = input("Enter filename: ")

def rot13(text):
    abc = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for c in text:
        if c.lower() in abc:
            # Find index in alphabet and add 13
            idx = abc.index(c.lower())
            new_c = abc[(idx + 13) % 26]
            
            if c.isupper():
                new_c = new_c.upper()
            result += new_c
        else:

            result += c

    return result

with open(filename, 'r') as f:
    content = f.read()

with open(filename, 'w') as f:
    f.write(rot13(content))