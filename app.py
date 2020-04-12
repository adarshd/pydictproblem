import json

data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[w]

word = input("Enter word: ")


print(translate(word))

