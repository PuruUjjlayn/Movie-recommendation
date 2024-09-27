import pickle
import streamlit as st
import pandas as pd

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

# Streamlit UI
st.header('Movie Recommender System')
movies_dict = pickle.load(open(r'C:\Users\puruc\Downloads\Movie_Recommender_System\movie_dict.pkl', 'rb'))
similarity = pickle.load(open(r'C:\Users\puruc\Downloads\Movie_Recommender_System\similarity.pkl', 'rb'))

movies = pd.DataFrame(movies_dict)
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    st.write("### Recommendations:")
    for i, name in enumerate(recommended_movie_names, start=1):
        st.write(f"{i}. {name}")