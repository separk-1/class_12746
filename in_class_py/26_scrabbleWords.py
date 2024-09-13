# %%
scrabbleFile=open('Lecture5/words.txt', 'r')
for i in range(5):
    nextLine = scrabbleFile.readline()
    nextWord = nextLine.strip() # strip removes white spaces
    print(nextWord)
scrabbleFile.close()
# %%
