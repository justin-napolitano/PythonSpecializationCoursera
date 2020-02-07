
#For each word in the list verbs, add an -ing ending. Save this new list in a new list, ing

verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing = []
for verb in range(len(verbs)):
    ing.append(verbs[verb] + 'ing')


#Given the list of numbers, numbs, create a new list of those same numbers increased by 5. Save this new list to the variable newlist.
numbs = [5, 10, 15, 20, 25]
newlist=[]
for i in range(len(numbs)):
   newlist.append(numbs[i]+5)
print(newlist)


#Challenge Now do the same as in the previous problem, but do not create a new list. Overwrite the list numbs so that each of the original numbers are increased by 5.
numbs = [5, 10, 15, 20, 25]
for i in range(len(numbs)):
   numbs[i] = numbs[i] + 5

#For each number in lst_nums, multiply that number by 2 and append it to a new list called larger_nums.
lst_nums = [4, 29, 5.3, 10, 2, 1817, 1967, 9, 31.32]
larger_nums = []
for i in range(len(lst_nums)):
    larger_nums.append(lst_nums[i]*2)
