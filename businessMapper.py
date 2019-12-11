#!/usr/bin/python

#business mapper.py
#Richard Pham, Jonathan Nguyen, Zhihang Yao
#get all good businesses and print their category, city, and state

import json
import sys


# good_businesses = {} 
# with open("good_businesses.txt") as f:
    # for line in f:
        # ID, score = line.split("\t")
        # try:
            # score = float(score)
        # except ValueError:
            # continue
        # good_businesses[ID] = score
    
#the minimum average star rating
starsThreshold = 4.0

#the minimum number of reviews 
reviewsThreshold = 50

#iterate through each line in sys.stdin
for line in sys.stdin:
    line = line.strip()
    
    #line interpreted as a json object, returns a dictionary 
    b = json.loads(line)
    
    #check if business actually exists 
    if b is not None:
    
        try:
            #check if categories, stars, review_count is in business json object 
            if 'categories' in b and 'stars' in b and 'review_count' in b:
                stars = b['stars']
                review_count = b['review_count']
                
                #try and convert stars and review_count to float and int 
                try:
                    stars = float(stars)
                    review_count = int(review_count)
                except ValueError:
                    continue
                
                #check if business is good (review_count >= 50, stars >= 4)
                if review_count >= reviewsThreshold and stars >= starsThreshold:
                    #get list of all categories business falls under 
                    categories = b['categories'].split(', ')
                    #iterate through each category 
                    for i in range(len(categories)):
                        #try-catch in case city or state does not exist 
                        try:
                            #prints each category, city, and state (passed into reducer.py)
                            print(categories[i] + "\t" + b["city"] + ", " + b["state"])
                        except KeyError:
                            continue
        except:
            continue

