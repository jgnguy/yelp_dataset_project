# yelp_dataset_project

# Capstone Project - Yelp Dataset
This is our Capstone Project for our Big Data and Cloud Computing class. We used the Yelp dataset (http://www.yelp.com/dataset_challenge) and wanted to find the best city to go to for each Yelp category. For example, find the city with the best hamburgers, bookstores, arcades, etc. This was ran using a Hadoop cluster on AWS EMR and utilized Amazon S3 for storage. 


## Running MapReduce
First, in order to run our programs, one must have an AWS account and create an S3 bucket. Then, store the mapper and reducer programs and the business.json and review.json files within the Yelp dataset. Next, create a cluster on AWS EMR, specifically choosing to create a Hadoop cluster. After the cluster initializes, go to Steps. Press on the 'Add Step' button and specify the 'Step type' to 'Streaming program'. Afterwards, input in the mapper and reducer programs in the specified fields. Insert the JSON file location in the 'Input S3 location', and then, insert the output location (must be specified as a new folder that has not been created yet). Finally, press on 'Add' on the bottom-right, and the output of EMR will be saved to the output location.

## Contributors
* **Richard Pham**, **Jonathan Nguyen**, **Zhihang Yao (Evan)**
