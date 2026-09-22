import csv
def load_imdb_top_rated(filename:str)->list:#gets top rated movies
    top_rated = []
    with open(filename, "r", encoding = "utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            top_rated.append(row)
        return top_rated

def load_imdb_top_grossing(filename:str)->list:#gets the list of top grossing movies
    top_gross = []
    with open(filename, "r", encoding = "utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            top_gross.append(row)
        return top_gross

def load_imdb_top_casts(filename:str)->list:
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

def movieInTopRated(movie:str, topMovies:list)->bool:#checking a given move is in the top rated movies
    for aMovie in topMovies:
        if movie == aMovie[1]:
            return True
    return False

def disply_top_collaborations(casts:list,topMovies:list):
    i = 0
    collabs = {}
    #creating a nested dictionary to store directors with actors and collaboration counts
    for movie in casts:
        title = movie[0]
        director = movie[2]
        actors = movie[3]
        if movieInTopRated(title,topMovies):
            directors = collabs.get(director, {})
            
            for actor in actors:
                directors[actor] = directors.get(actor,0) + 1
            collabs[director] = directors

    return collabs

def top10(collabs)->tuple:#gets the actors and collaborations with 
    collaborations = []
    for director in collabs:#putting the directors,actors, and collabs in a tuple
        for actor in collabs[director]:
            count = collabs[director][actor]
            collaborations.append((director, actor, count))
    #sorting the tuple by most collabs
    for i in range(len(collaborations)):
        max = i
        for j in range(i+1, len(collaborations)):
            if collaborations[j][2] > collaborations[max][2]:
                max = j
        temp = collaborations[i]
        collaborations[i] = collaborations[max]
        collaborations[max] = temp
    top10 = tuple(collaborations[:10])
    return top10
def getActorsGross(casts:list, topGrossing:list): #returns
    actorGross = {}
    for aMovie in casts:#gettings the movies
        title = aMovie[0]
        actors = aMovie[3]

        for movie in topGrossing:# getting the movies from top grossing
            if title == movie[1]:# only continues if the movie is in the list
                gross = int(movie[3])
                for actor in actors:
                    actorGross[actor] = actorGross.get(actor,0) + gross
                
        actorList = list(actorGross.items())
        for i in range(len(actorList)):
                max = i
                for j in range(i+1, len(actorList)):
                    if actorList[j][1] > actorList[max][1]:
                        max = j
                temp = actorList[i]
                actorList[i] = actorList[max]
                actorList[max] = temp
        return actorGross

topMovies = load_imdb_top_rated("imdb-top-rated.csv")
topGrossingMovies = load_imdb_top_grossing("imdb-top-grossing.csv")
topCasts = load_imdb_top_casts("imdb-top-casts.csv")
directorCollabs = (disply_top_collaborations(topCasts, topMovies))

print(directorCollabs)
for i in top10(directorCollabs):
    print(i)

print(getActorsGross(topCasts, topGrossingMovies))
