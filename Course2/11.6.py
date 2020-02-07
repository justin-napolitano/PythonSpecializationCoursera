11.6 Introduction: Accumulating Multipile Results in a Dictionary


f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
x = {} # start with an empty dictionary
for c in txt:
    if c not in x:
        # we have not seen this character before, so initialize a counter for it
        x[c] = 0

    #whether we've seen it before or not, increment its counter
    x[c] = x[c] + 1

print("t: " + str(x['t']) + " occurrences")
print("s: " + str(x['s']) + " occurrences")



for c in letter_counts.keys():
    print(c + ": " + str(letter_counts[c]) + " occurrences")

#2 Provided is a string saved to the variable name sentence. Split the string into a list of words, then create a dictionary that contains each word and the number of times it occurs. Save this dictionary to the variable name word_counts.
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
words = sentence.split()
#print(words)
word_counts = {}
for word in words:
    if word not in word_counts:
        word_counts[word] = 0

    word_counts[word] = word_counts[word] + 1


#3 Create a dictionary called char_d from the string stri, so that the key is a character and the value is how many times it occurs.
stri = "what can I do"
char_d = {}
for c in stri:
    if c not in char_d:
        char_d[c] = 0
    char_d[c] = char_d[c] + 1
