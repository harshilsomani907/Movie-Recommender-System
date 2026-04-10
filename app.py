import streamlit as st
import pickle
import pandas as pd
import requests
import numpy as np   # NEW: used for datatype conversion

# Function to fetch movie poster from TMDB API
def fetch_poster(movie_id):
  response =  requests.get('https://api.themoviedb.org/3/movie/{}?api_key=252109b8503f3ece166de53216049d8c&language=en-US'.format(movie_id))  # existing API request
  data = response.json()  # convert response to json
  return "https://image.tmdb.org/t/p/w500/" + data['poster_path']  # return full poster URL

# Function to recommend movies based on similarity matrix
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # find index of selected movie
    distances = similarity[movie_index]  # get similarity scores for that movie
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1: 6]  # sort and take top 5

    recommended_movie = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id  # get movie id
        # fetch poster from api
        recommended_movie.append((movies.iloc[i[0]].title))  # append movie title
        recommended_movies_posters.append(fetch_poster(movie_id))  # append poster url
    return recommended_movie,recommended_movies_posters


# Load movie dictionary file
movies_dict  = pickle.load(open('movies_dict.pkl', 'rb'))  # existing command

# Load similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))  # existing command

# NEW: reduce memory usage by converting similarity matrix to float32
similarity = np.array(similarity).astype(np.float32)

# Convert dictionary to pandas dataframe
movies = pd.DataFrame(movies_dict)

# Streamlit app title
st.title('Movie recommender system')

# Dropdown to select movie
selected_movie_name = st.selectbox('Select an option', movies['title'].values)

# When recommend button is clicked
if st.button('recommend'):
   names,posters =  recommend(selected_movie_name)
   col1, col2, col3, col4, col5 = st.columns(5)  # create 5 columns

   with col1:
       st.text(names[0])  # show movie name
       st.image(posters[0])  # show poster
   with col2:
       st.text(names[1])
       st.image(posters[1])
   with col3:
       st.text(names[2])
       st.image(posters[2])
   with col4:
       st.text(names[3])
       st.image(posters[3])
   with col5:
       st.text(names[4])
       st.image(posters[4])
