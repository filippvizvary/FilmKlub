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
    prikaz=input('Enter command(type help for commands): ').strip().lower()
    if prikaz=='help':
        print('V-list all movies\nH-rate a movie\nA-Add a movie\nF-filter by genre\nY-filter by year\nZ-list genres\nT-top movies\nS-search movies\nM-my genres\nR-recommend movies\nP-profile\nQ-quit')

    if prikaz=='v':
        for i in range(len(filmy)):
            print(f'{i+1}. {filmy[i][0]} ({filmy[i][2]}) - {filmy[i][1]} - {filmy[i][3]} min - Rating: {filmy[i][4]}')

    if prikaz=='h':
        meno=input('Enter your name: ').strip().capitalize()
        nazov=input('Enter movie name: ').strip().capitalize()
        hodnotenie=int(input('Enter rating (1-10): ')).strip()
        hodnotenia.append((meno, nazov, hodnotenie))
        print(f'Rating added: {meno} rated {nazov} with {hodnotenie}/10')

    if prikaz=='a':
        nazov=input('Enter movie name: ').strip().capitalize()
        zaner=input('Enter genre: ').strip().lower()
        rok=int(input('Enter release year: ')).strip()
        dlzka=int(input('Enter duration (minutes): ')).strip()
        rating=float(input('Enter rating (1-10): ')).strip()
        filmy.append((nazov, zaner, rok, dlzka, rating))
        print(f'Movie added: {nazov} ({rok}) - {zaner} - {dlzka} min - Rating: {rating}')

    if prikaz=='f':
        sorted_filmy = []
        zaner=input('Enter genre to filter by: ').strip().lower()
        for film in filmy:
            if film[1].lower() == zaner:
                sorted_filmy.append(film)
        for film in sorted_filmy:
            print(f'{film[0]} ({film[2]}) - {film[1]} - {film[3]} min - Rating: {film[4]}')
        if len(sorted_filmy) == 0:
            print(f'No movies found in genre: {zaner}')

    
    if prikaz=='y':
        sorted_filmy = []
        rok=int(input('Enter release year to filter by: ').strip())
        for film in filmy:
            if film[2] == rok:
                sorted_filmy.append(film)
        for film in sorted_filmy:
            print(f'{film[0]} ({film[2]}) - {film[1]} - {film[3]} min - Rating: {film[4]}')
        if len(sorted_filmy) == 0:
            print(f'No movies found from year: {rok}')
    
    if prikaz=='z':
        zanre = set(film[1] for film in filmy)
        print('Available genres:')
        for zaner in zanre:
            print(f' - {zaner}')

    if prikaz=='t':
        top_filmy = sorted(filmy, key=lambda x: x[4], reverse=True)[:5]
        print('Top 5 movies:')
        for film in top_filmy:
            print(f'{film[0]} ({film[2]}) - {film[1]} - {film[3]} min - Rating: {film[4]}')

    if prikaz=='s':
        search_term = input('Enter movie name to search for: ').strip().lower()
        found_filmy = [film for film in filmy if search_term in film[0].lower()]
        if found_filmy:
            print('Search results:')
            for film in found_filmy:
                print(f'{film[0]} ({film[2]}) - {film[1]} - {film[3]} min - Rating: {film[4]}')
        else:
            print(f'No movies found with name containing: {search_term}')

    if prikaz=='m':
        meno=input('Enter your name: ').strip().capitalize()
        user_ratings = [h for h in hodnotenia if h[0] == meno]
        if user_ratings:
            genres = set()
            for rating in user_ratings:
                movie_name = rating[1]
                for film in filmy:
                    if film[0] == movie_name:
                        genres.add(film[1])
            print(f'{meno}\'s favorite genres:')
            for genre in genres:
                print(f' - {genre}')
        else:
            print(f'No ratings found for user: {meno}')

    if prikaz=='r':
        meno=input('Enter your name: ').strip().capitalize()
        user_ratings = [h for h in hodnotenia if h[0] == meno]
        if user_ratings:
            genres = set()
            for rating in user_ratings:
                movie_name = rating[1]
                for film in filmy:
                    if film[0] == movie_name:
                        genres.add(film[1])
            recommended_films = [film for film in filmy if film[1] in genres and film[0] not in [r[1] for r in user_ratings]]
            if recommended_films:
                print(f'Movies recommended for {meno}:')
                for film in recommended_films:
                    print(f'{film[0]} ({film[2]}) - {film[1]} - {film[3]} min - Rating: {film[4]}')
            else:
                print(f'No recommendations available for {meno}')
        else:
            print(f'No ratings found for user: {meno}')

    if prikaz=='p':
        meno=input('Enter your name: ').strip().capitalize()
        user_ratings = [h for h in hodnotenia if h[0] == meno]
        if user_ratings:
            print(f'{meno}\'s profile:')
            for rating in user_ratings:
                print(f' - {rating[1]}: {rating[2]}/10')
        else:
            print(f'No ratings found for user: {meno}')

    if prikaz=='q':
        print('Goodbye!')
        break