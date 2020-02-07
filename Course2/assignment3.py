#Assignment3.py
#1 The dictionary Junior shows a schedule for a junior year semester. The key is the course name and the value is the number of credits. Find the total number of credits taken this semester and assign it to the variable credits. Do not hardcode this – use dictionary accumulation!
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0
for course in Junior:
    credits = Junior.get(course) + credits


#2 Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.
str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for ch in str1:
    if ch not in freq:
        freq[ch] = 0
    freq[ch] = freq[ch] + 1

#3Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.
s1 = "hello"
counts = {}
for ch in s1:
    if ch not in counts:
        counts[ch] = 0
    counts[ch] = counts[ch] +1
#4 Create a dictionary, freq_words, that displays each word in string str1 as the key and its frequency as the value.

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] = counts[word] +1

    return counts

freq_words = word_count(str1)

#5 Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many times you have seen that word.
sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] = counts[word] +1

    return counts

wrd_d = word_count(sent)


#6  Create the dictionary characters that shows each character from the string sally and its frequency. Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.
def char_count(str):
    counts = dict()
    characters = str
    for ch in characters:
        if ch not in counts:
            counts[ch] = 0
        counts[ch] = counts[ch] + 1

    return counts

def most_freq(dict):
    ks = dict.keys()
    max_value = list(ks)[0]

    for k in ks:
        if dict[k] > dict[max_value]:
            max_value = k

    return max_value


sally = "sally sells sea shells by the sea shore"

characters = char_count(sally)
best_char = most_freq(characters)


#7 Do the same as above but now find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency. Then, find the least frequent letter in the string and assign the letter to the variable worst_char.

def char_count(str):
    counts = dict()
    characters = str
    for ch in characters:
        if ch not in counts:
            counts[ch] = 0
        counts[ch] = counts[ch] + 1

    return counts

def least_freq(dict):
    ks = dict.keys()
    min_value = list(ks)[0]

    for k in ks:
        if dict[k] < dict[min_value]:
            min_value = k

    return min_value


sally = "sally sells sea shells by the sea shore and by the road"

characters = char_count(sally)
worst_char = least_freq(characters)


#8 Create a dictionary named letter_counts that contains each letter and the number of times it occurs in string1. Challenge: Letters should not be counted separately as upper-case and lower-case. Intead, all of them should be counted as lower-case.

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."


def counting(str):
    counting = str.lower()
    counts = dict()
    for ch in counting:
        if ch not in counts:
            counts[ch] = 0
        counts[ch] = counts[ch] + 1
    return counts

letter_counts = counting(string1)

#9 Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each character was seen. Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."

def counting(str):
    counting = str.lower()
    counts = dict()
    for ch in counting:
        if ch not in counts:
            counts[ch] = 0
        counts[ch] = counts[ch] + 1
    return counts

low_d = counting(p)
