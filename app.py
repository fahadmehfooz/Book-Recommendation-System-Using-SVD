import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from scipy.sparse.linalg import svds
from flask import Flask, render_template, request
import pickle

d = pickle.load(open("d.p", "rb"))
with open('Vt','rb') as f: Vt = pickle.load(f)
book_user_rating =  pickle.load(open("book_user_rating.pkl", "rb"))
np.seterr(divide='ignore', invalid='ignore')


def top_cosine_similarity(data, book_id, top_n=10):
    index = book_id 
    book_row = data[index, :]
    magnitude = np.sqrt(np.einsum('ij, ij -> i', data, data))
    similarity = np.dot(book_row, data.T) / (magnitude[index] * magnitude)
    sort_indexes = np.argsort(-similarity)
    return sort_indexes[:top_n]

def similar_books(book_user_rating, book_id, top_indexes):
    l = []
    print('Recommendations for {0}: \n'.format(
    book_user_rating[book_user_rating.unique_id_book == book_id]['Book-Title'].values[0]))
    for id in top_indexes + 1:
        l.append(book_user_rating[book_user_rating.unique_id_book == id]['Book-Title'].values[0])
    return l


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():

    if request.method == 'POST':
        try:
            message = request.form['message']       
            index = top_cosine_similarity(Vt.T[:, :50], int(message) , 3)

            my_prediction = similar_books(book_user_rating,int(message) ,index)
            s= {}

            for i in range(len(my_prediction)):
                s[i+1]= my_prediction[i]
                
            return render_template('result.html',prediction = s)
        except:
            return render_template('result.html',prediction = {'Error': 'Invalid ISBN number, enter correct ISBN please! '})

if __name__ == '__main__':
    app.run(debug=False)