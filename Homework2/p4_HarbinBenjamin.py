import csv
def load_imdb_top_rated(filename):
    with open(filename, "r", encoding = "utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

load_imdb_top_rated("imdb-top-rated.csv")