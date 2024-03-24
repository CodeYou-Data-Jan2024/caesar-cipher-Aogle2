# add your code here
def cipher():
    result = ""
    original_sentence = input() 
    shift = 5
    for char in original_sentence:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - base + shift) % 26 + base)
            result += shifted
        else:
            result += char
    return('The encrypted sentence is: ' + result.lower())

cipher()