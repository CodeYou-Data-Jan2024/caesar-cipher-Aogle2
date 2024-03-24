# add your code here
def cipher(text: str =input()):
    result = "" 
    shift = 5
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - base + shift) % 26 + base)
            result += shifted
        else:
            result += char
    return('The encrypted sentence is: ' + result.lower())