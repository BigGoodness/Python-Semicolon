def removeConsonant():
    data=input("enter a string to remove odd index from string: ")
    vowels="aeiouAEIOU"
    return "".join(c for c in data if c in vowels)



print(removeConsonant())

