import pandas as pd 

df = pd.read_csv("./Day26/nato_phonetic_alphabet.csv")


name_list = {row[0]:row[1] for (index, row) in df.iterrows()}

word = input("Please input a word: ").upper()
out = [name_list[letter] for letter in word]
print(out)