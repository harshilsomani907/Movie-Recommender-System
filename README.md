# 🎬 Movie Recommender System

This project is a **Movie Recommendation System** built using **Python and Streamlit**.  
It recommends movies similar to the selected movie using a **content-based recommendation algorithm with cosine similarity**.

The application provides an interactive interface where users can select a movie and receive similar movie suggestions along with their posters.

---

## 🚀 Live Demo

Try the application here:

Live App:  
https://movie-recommender-system-9pvagl6jvrba9jlyzs8n29.streamlit.app/

Source Code:  
https://github.com/harshilsomani907/Movie-Recommender-System

---

## ✨ Features

- Select a movie from the dropdown list
- Get top 5 similar movie recommendations
- Display movie posters using TMDB API
- Interactive web interface built with Streamlit
- Fast recommendation using cosine similarity

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- TMDB API

---

## ⚙️ How It Works

1. Movie data is processed using **CountVectorizer**.
2. A **cosine similarity matrix** is generated between movies.
3. When a user selects a movie, the system finds the most similar movies.
4. Movie posters are fetched using the **TMDB API**.

---

## ▶️ Run the Project Locally

Install dependencies:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run app.py

---

## 📂 Project Structure

Movie-Recommender-System
│
├── app.py               # Streamlit application
├── movies.pkl           # Movie dataset
├── movies_dict.pkl      # Processed movie dictionary
├── requirements.txt     # Python dependencies
└── README.md

---

## 👨‍💻 Author

Harshil Somani

GitHub:  
https://github.com/harshilsomani907
