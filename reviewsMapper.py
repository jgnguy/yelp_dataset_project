#!/usr/bin/python

#REVIEWS mapper.py
#Evan Yao, Jonathan Nguyen, Richard Pham
#get all the stars and businessID of all businesses within a specified number of years ago 

import datetime
import json
import sys

#get today's date and convert to YYYY-MM-DD format
numYearsAgo = 2
today = datetime.datetime.now()
#get a year ago from today
yearAgo = today - datetime.timedelta(numYearsAgo * 365)
reformatYear = yearAgo.strftime('%Y-%m-%d')
pastYear, pastMonth, pastDay = reformatYear.split('-')
pastYearDate = datetime.datetime(int(pastYear), int(pastMonth), int(pastDay))

#adds each review to a list
for line in sys.stdin:
    line = line.strip()
    review = json.loads(line)
    #check if review exists
    if review is not None:
      try:
        reviewDate = review['date']
        reviewYear, reviewMonth, reviewDay = reviewDate.split(' ')[0].split('-')
        refReviewDate = datetime.datetime(int(reviewYear), int(reviewMonth), int(reviewDay))  
        #check if review is relevant and current
        if pastYearDate < refReviewDate:
            #print the business ID the review is for and the amount of stars they gave
            print(review['business_id'] + '\t' + str(review['stars']))
      except:
        continue
