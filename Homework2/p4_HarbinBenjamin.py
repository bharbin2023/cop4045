import csv
def load_imdb_top_rated(filename):
    top_rated = []
    with open(filename, "r", encoding = "utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            top_rated.append(row)
        return top_rated
def load_imdb_top_grossing(filename):
    top_gross = []
    with open(filename, "r", encoding = "utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            top_gross.append(row)
        return top_gross
def load_imdb_top_casts(filename):
    top_casts = []
    with open(filename, "r", encoding = "utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            tempList = []
            tempList.append(row[0])#title
            tempList.append(row[1])#year
            tempList.append(row[2])#director
            tempList.append(row[3:])#Actors

            top_casts.append(tempList)
        return top_casts
def movieInTopRated(movie:str, topMovies:list)->bool:
    for aMovie in topMovies:
        if movie == aMovie[1]:
            return True
    return False

def disply_top_collaborations(casts:list,topMovies:list):
    i = 0
    collabs = {}
    for movie in casts:
        title = movie[0]
        director = movie[2]
        actors = movie[3]
        if movieInTopRated(title,topMovies):
            directors = collabs.get(director, {})
            
            for actor in actors:
                directors[actor] = directors.get(actor,0) + 1
            collabs[director] = directors
    for directors in collabs:
        actors = list(collabs[director].items())
        for i in range(len(actors)):
            max = i
            for j in range(i+1, len(actors)):
                if actors[j][1] > actors[max][1]:
                    max = j
            temp = actors[i]
            actors[i] = actors[max]
            actors[max] = temp
    collabs[director] = dict(actors)
    print(collabs)
    return collabs


topMovies = load_imdb_top_rated("imdb-top-rated.csv")
topGrossingMovies = load_imdb_top_grossing("imdb-top-grossing.csv")
topCasts = load_imdb_top_casts("imdb-top-casts.csv")
directorCollabs = (disply_top_collaborations(topCasts, topMovies))
print(directorCollabs)
