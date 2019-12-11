#!/usr/bin/python

#business reducer
#Richard Pham, Jonathan Nguyen, Zhihang Yao
#gives top city for each category 

import sys

dictionary = {}

#iterate through each line of stdin
for line in sys.stdin:
    line = line.strip()
    #add each line to dictionary, increment counter if line is found in dictionary 
    if line in dictionary:
        dictionary[line] += 1
    else:
        dictionary[line] = 1

    
    
#sort list based on counter, most to least 
sorted_list = sorted(dictionary, key = dictionary.get, reverse=True)

#sort previous list based on category, alphabetical order
sorted_list.sort(key = lambda entry: str(entry.split('\t')[0]))

#final list object
finalList = []


currentCategory = None

#iterate through each object in sorted list 
for entry in sorted_list:
    #get the category 
    entryCat = entry.split("\t", 1)[0]
    #check if null
    if currentCategory is None:
      #add to list and set currentCategory
      finalList.append(entry)
      currentCategory = entryCat
    else:
      #if new category 
      if currentCategory != entryCat:
        #add to list 
        finalList.append(entry)
        currentCategory = entryCat

#iterate through finalList and print each entry and its counter 
for k in finalList:
    print(k + "\t" + str(dictionary[k]))


