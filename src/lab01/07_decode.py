text = input("in: ")
start = [i.isupper() for i in text].index(True)
second = [i.isdecimal() for i in text].index(True, start) + 1
print(text[start :: second - start])
