from fastapi import FastAPI

from .model import get_recommend_movie

app = FastAPI()


@app.get("/recommend/{movie_name}", )
async def recommend(movie_name: str):
    return {"data": get_recommend_movie(movie_name)}
