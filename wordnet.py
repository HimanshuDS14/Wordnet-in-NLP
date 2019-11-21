from nltk.corpus import wordnet

name = input("Enter a word which you want to get their synonyms and their example and definition   : ")

syns = wordnet.synsets(name)
print(syns)

for i in syns:
    print(i.name())

print("\n\n")
print("...........definition................")
#definition of all syns
for i in syns:
    print(f"{i.name()} ---> {i.definition()} " )
print("\n\n")
print(".................Examples.....................")
#example
for i in syns:
   print(f"{i.name()} ---> {i.examples()}")