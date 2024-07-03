import pandas as pd

df = pd.read_csv("./nato_phonetic_alphabet.csv")
# print([df.code.to_list()[df.letter.to_list().index(item)] for item in [letter for letter in input("Enter a word: ").upper()] if item in df.letter.to_list()])

word = input("give a word: ").upper()
dictionary = {row.letter:row.code for (index, row) in df.iterrows()}
outputlist = [dictionary[letter] for letter in word]
print(outputlist)