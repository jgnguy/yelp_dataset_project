#!/usr/bin/python

#REVIEWS reducer.py
#Evan Yao, Jonathan Nguyen, Richard Pham
#count up all the reviews of 4 stars of more of each businessID 

import sys

dictTotalStars = {}
dictTotalCount = {}
dictGoodBusinesses = {}

starsThreshold = 4.0

#iterate through each line
for line in sys.stdin:
    line = line.strip()
    #get businessID and stars
    businessID, stars = line.split('\t')
    #make sure stars is correctly formatted
    try:
      stars = float(stars)
    except ValueError:
      continue
      
    #add up the stars of each businessID 
    if businessID not in dictTotalStars:
      dictTotalStars[businessID] = stars
    else: 
      dictTotalStars[businessID] += stars
    #add up the reviews of each businessID
    if businessID not in dictTotalCount:
      dictTotalCount[businessID] = 1
    else:
      dictTotalCount[businessID] += 1

#iterate through each business
for business in dictTotalStars:
  #get the average stars given by reviews for each business
  businessAverageStars = dictTotalStars[business] / dictTotalCount[business]
  
  #check if the average stars is greater than or equal to 4
  if businessAverageStars >= starsThreshold:
    #add to dictionary of good businesses
    dictGoodBusinesses[business] = businessAverageStars
      

#print all good businesses
for business in dictGoodBusinesses:
  print(business + "\t" + str(dictGoodBusinesses[business]))
    