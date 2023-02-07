def high_score(movie):
    return movie["imdb"] > 5.5
        

print(high_score({"name": "Usual Suspects","imdb": 7.0,"category": "Thriller"}))