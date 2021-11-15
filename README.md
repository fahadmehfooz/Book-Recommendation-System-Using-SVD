# Book-Recommendation-System-Using-SVD: Project Overview

* Joined the user rating and book dataframes.
* Created unique id for every ISBN, as later on when entering an on app it would be easier for the user.
* Built a pivot matrix of user ids and unique ids.
* Built a collaborative recommendation system.
* Used Decomposition vectors as 15, as more the factors higher information can be retained when combining the matrix.
* Wrote a function to find top cosine similarity and return the similar books.
* For every book top 3 similar books would be returned.
* Created an app on Flask and deployed it on Heroku.


## Languages Used 
**Python Version:** 3.9.0

## Resources and Tools Used
**Tools:** Jupyter Notebook

**Packages:** Pandas, NumPy, nltk and scipy.  

## Data Used
* Books are identified by their respective ISBN. Invalid ISBNs have already been removed from the dataset. Moreover, some content-based information is given (Book-Title, Book-Author, Year-Of-Publication, Publisher), obtained from Amazon Web Services.
*  Note that in case of several authors, only the first is provided. URLs linking to cover images are also given, appearing in three different flavours (Image-URL-S, Image-URL-M, Image-URL-L), i.e., small, medium, large. These URLs point to the Amazon web site.
* **Data taken from kaggle** : https://www.kaggle.com/fahadmehfoooz/book-recommendation-system/data

## Data Wrangling and Data Visualization
* Joined the user rating and book dataframes.
* Created unique id for every ISBN, as later on when entering an on app it would be easier for the user.
* Built a pivot matrix of user ids and unique ids.

## App:

https://book-recommendation-system-svd.herokuapp.com/
