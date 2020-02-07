#10.4. Iterating over lines in a file
#The efficient way to iterate over lines in a files
olypmicsfile = open("olypmics.txt","r")

for aline in olypmicsfile:
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olypmicsfile.close()


#1Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.
fileref = open('emotion_words.txt','r')
num_lines = 0
for line in fileref:
    num_lines +=1
