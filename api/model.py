import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

merged_df = pd.read_pickle("models/merged.pkl")
movies = pd.read_pickle("models/movies.pkl")
cv = CountVectorizer(max_features=movies.shape[0], stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()
similarity = cosine_similarity(vectors)


def get_recommend_movie(movie_name):
    res = []
    movie_idx = movies[movies['title'] == movie_name].index[0]
    distances = sorted(
        list(enumerate(similarity[movie_idx])), reverse=True, key=lambda x: x[1])[1:6]
    for i in distances:
        movie_id = i[0]
        res.append({"name": movies.iloc[movie_id].title,
                   'details': merged_df.iloc[movie_id].to_json(indent=False)})
    return res
