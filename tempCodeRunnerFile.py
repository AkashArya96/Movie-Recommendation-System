import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2e134cfbc1bb5e1f72d06c3a8a75d85e'.format(movie_id))
    data = response.json()
    return data['poster_path']




def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        #fetch poster 
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))
 
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'How would you like to be contacted?',
movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)