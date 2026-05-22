filmy = [ 
    ("Inception",        "sci-fi",   2010, 148, 8.8), 
    ("Parasite",         "thriller", 2019, 132, 8.6), 
    ("Spirited Away",    "anime",    2001, 125, 8.6), 
    ("Pulp Fiction",     "crime",    1994, 154, 8.9), 
    ("Mad Max Fury Road","action",    2015, 120, 8.1), 
    ("The Matrix",       "sci-fi",   1999, 136, 8.7), 
    ("Whiplash",         "drama",    2014, 106, 8.5), 
    ("Get Out",          "thriller", 2017,  104, 7.7), 
    ("Interstellar",     "sci-fi",   2014, 169, 8.7), 
    ("La La Land",       "drama",    2016, 128, 8.0), 
    ("Joker",            "drama",    2019, 122, 8.4), 
    ("Knives Out",       "crime",    2019, 130, 7.9), 
    ("Your Name",        "anime",    2016, 106, 8.4), 
    ("John Wick",        "action",   2014, 101, 7.4), 
    ("The Grand Budapest Hotel","comedy",2014,99, 8.1),
]

hodnotenia = [ 
    ("Jana",  "Inception",     9), 
    ("Jana",  "The Matrix",    10), 
    ("Mia",   "Parasite",      10), 
    ("Mia",   "Spirited Away", 9), 
    ("Petra", "Whiplash",      8), 
    ("Petra", "La La Land",    7), 
    ("Adam",  "Pulp Fiction",  10), 
    ("Adam",  "Knives Out",     8), 
    ("Tomas", "John Wick",     7), 
    ("Tomas", "Mad Max Fury Road", 9),
    ("Jana",  "Joker",         7), 
    ("Mia",   "Your Name",     10), 
    ("Petra", "The Grand Budapest Hotel", 9), 
    ("Adam",  "Get Out",       8), 
    ("Tomas", "Interstellar",  10), 
]

while True:
    prikaz=input('Enter command(type help for commands): ')
    if prikaz=='help':
        print('V-list all movies\nH-rate a movie\nA-Add a movie\nF-filter by genre\nQ-quit')

    
