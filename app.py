import streamlit as st
import pickle
import pandas as pd
from PIL import Image
im = Image.open('book.png')

st.set_page_config(page_title="",layout='wide', page_icon=im)

st.title(':yellow[Book Recommendation Engine]')


book_list=pickle.load(open('books.pkl','rb'))
similarity_list=pickle.load(open('similarities.pkl','rb'))
books=pd.DataFrame(book_list)

def book_recommender(book):
    book_index=books[books['title']==book].index[0]
    distances=sorted(list(enumerate(similarity_list[book_index])),reverse=True, key=lambda x:x[1])[1:11]
    book_and_img =[]
    for i in distances:
        book_and_img.append({'title':books.iloc[i[0]]['title'],'link':books.iloc[i[0]]['thumbnail']})
    return book_and_img

book_selected=st.selectbox('',(books['title']))


if st.button('Gimme Gimme More...'):
    b_img_list=book_recommender(book_selected)
    columns = st.columns(5)  
    for i, image_data in enumerate(b_img_list):
        with columns[i % 5]: 
            st.image(image_data['link'], use_column_width=True)
            st.caption(image_data["title"])
