movies = [ 
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

ratings = [ 
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

my_genres = set()

while True:
    command=input('Enter command(type help for commands): ').strip().lower()
    if command=='help':
        print('V-list allmovies\nH-rate a movie\nA-Add a movie\nF-filter by genre\nY-filter by year\nZ-list genres\nT-top movies\nS-search movies\nM-my genres\nR-recommend movies\nP-profile\nQ-quit')

    if command=='v':
        for i in range(len(movies)):
            print(f'{i+1}. {movies[i][0]} ({movies[i][2]}) - {movies[i][1]} - {movies[i][3]} min - Rating: {movies[i][4]}')

    if command=='h':
        member_name=input('Enter your name: ').strip().capitalize()
        title=input('Enter movie name: ').strip().capitalize()
        found=False
        for movie in movies:
            if movie[0]==title:
                found=True
                break
        if not found:
            print('Movie npt found')
        else:
            while True:
                rating_str=input('Enter rating (1-10): ').strip()
                if rating_str.isdigit():
                    rating_value=int(rating_str)
                    if rating_value>=1 and rating_value<=10:
                        break
                print('Please enter a number between 1 and 10')
            ratings.append((member_name, title, rating_value))
            print(f'Rating added: {member_name} rated {title} with {rating_value}/10')

    if command == 'a':
        title=input('Enter movie name: ').strip().capitalize()
        genre=input('Enter genre: ').strip().lower()
        while True:
            year_str=input('Enter release year (1900-2025): ').strip()
            if year_str.isdigit():
                year=int(year_str)
                if year>=1900 and year<=2025:
                    break
            print('Please enter a year between 1900 and 2025')
        while True:
            duration_str=input('Enter duration (minutes): ').strip()
            if duration_str.isdigit():
                duration=int(duration_str)
                if duration>0:
                    break
            print('Please enter a positive number')
        while True:
            rating_str=input('Enter rating (1.0-10.0): ').strip()
            is_valid_float = False
            if rating_str.isdigit():
                is_valid_float = True
            elif rating_str.count('.') == 1:
                parts = rating_str.split('.')
                if parts[0].isdigit() and parts[1].isdigit():
                    is_valid_float = True
            
            if is_valid_float:
                rating_value=float(rating_str)
                if rating_value>=1.0 and rating_value<=10.0:
                    break
            print('Please enter a number between 1.0 and 10.0')
        movies.append((title, genre, year, duration, rating_value))
        print(f'Movie added: {title} ({year}) - {genre} - {duration} min - Rating: {rating_value}')

    if command=='f':
        filtered_movies = []
        genre=input('Enter genre to filter by: ').strip().lower()
        for movie in movies:
            if movie[1].lower() == genre:
                filtered_movies.append(movie)
        for movie in filtered_movies:
            print(f'{movie[0]} ({movie[2]}) - {movie[1]} - {movie[3]} min - Rating: {movie[4]}')
        if len(filtered_movies) == 0:
            print(f'No movies found in genre: {genre}')

    if command=='y':
        while True:
            start_year_str=input('Enter start year: ').strip()
            if start_year_str.isdigit():
                start_year=int(start_year_str)
                break
            print('Please enter a valid year')
        while True:
            end_year_str=input('Enter end year: ').strip()
            if end_year_str.isdigit():
                end_year=int(end_year_str)
                break
            print('Please enter a valid year')
        filtered_movies = []
        for movie in movies:
            if movie[2]>=start_year and movie[2]<=end_year:
                filtered_movies.append(movie)
        for movie in filtered_movies:
            print(f'{movie[0]} ({movie[2]}) - {movie[1]} - {movie[3]} min - Rating: {movie[4]}')
        if len(filtered_movies) == 0:
            print(f'No movies found between {start_year} and {end_year}')
    

    if command=='z':
        genres = set()
        for movie in movies:
            genres.add(movie[1])
        sorted_genres = sorted(genres)
        print('Available genres:')
        for genre in sorted_genres:
            print(f' - {genre}')

    if command=='t':
        top_movies = []
        for movie in movies:
            top_movies.append((movie[4], movie[0], movie[1], movie[2], movie[3]))
        for i in range(len(top_movies)-1):
            for j in range(len(top_movies)-i-1):
                if top_movies[j][0] < top_movies[j+1][0]:
                    temp_item = top_movies[j]
                    top_movies[j] = top_movies[j+1]
                    top_movies[j+1] = temp_item
        print('Top 5 movies:')
        counter=0
        for movie_item in top_movies:
            if counter<5:
                print(f'{movie_item[1]} ({movie_item[3]}) - {movie_item[2]} - {movie_item[4]} min - Rating: {movie_item[0]}')
                counter=counter+1

    if command=='s':
        search_term = input('Enter movie name to seaech for: ').strip().lower()
        found_movies = []
        for movie in movies:
            if search_term in movie[0].lower():
                found_movies.append(movie)
        if len(found_movies)>0:
            print('Search results:')
            for movie in found_movies:
                print(f'{movie[0]} ({movie[2]}) - {movie[1]} - {movie[3]} min - Rating: {movie[4]}')
        else:
            print(f'No movies found with name containing: {search_term}')

    if command=='m':
        sub_command=input('P=add genre, O=remove genre, V=view, S=back: ').strip().lower()
        if sub_command=='p':
            genre=input('Enter genre to add: ').strip().lower()
            my_genres.add(genre)
            print(f'Added {genre} to your genres')
        elif sub_command=='o':
            genre=input('Enter genre to remove: ').strip().lower()
            my_genres.discard(genre)
            print(f'Removed {genre} from your genres')
        elif sub_command=='v':
            print('Your favorite genres:')
            for genre in my_genres:
                print(f' - {genre}')
        elif sub_command=='s':
            pass

    if command=='r':
        if len(my_genres)==0:
            print('No favorite genres selected. Use M command to add genres.')
        else:
            recommended_movies = []
            for movie in movies:
                if movie[1] in my_genres and movie[4]>=7.5:
                    recommended_movies.append(movie)
            if len(recommended_movies)>0:
                print('Recommended movies:')
                for movie in recommended_movies:
                    print(f'{movie[0]} ({movie[2]}) - {movie[1]} - {movie[3]} min - Rating: {movie[4]}')
            else:
                print('No recommendations available')

    if command=='p':
        member_name=input('Enter your name: ').strip().capitalize()
        user_ratings = []
        for rating_entry in ratings:
            if rating_entry[0]==member_name:
                user_ratings.append(rating_entry)
        if len(user_ratings)>0:
            print(f'{member_name}\'s profile:')
            total_rating=0
            for rating_entry in user_ratings:
                print(f' - {rating_entry[1]}: {rating_entry[2]}/10')
                total_rating=total_rating+rating_entry[2]
            average_rating=total_rating/len(user_ratings)
            print(f'Average rating: {average_rating}')
        else:
            print(f'No ratings found for user: {member_name}')

    if command=='?':
        print('=== Most Active Critic ===')
        all_members = set()
        for rating_entry in ratings:
            all_members.add(rating_entry[0])
        max_rating_count=0
        most_active_member=''
        average_rating=0
        for member in all_members:
            rating_count=0
            total_rating=0
            for rating_entry in ratings:
                if rating_entry[0]==member:
                    rating_count=rating_count+1
                    total_rating=total_rating+rating_entry[2]
            if rating_count>0:
                member_average=total_rating/rating_count
                if rating_count>max_rating_count:
                    max_rating_count=rating_count
                    most_active_member=member
                    average_rating=member_average
        print(f'Most active: {most_active_member} ({max_rating_count} ratings, avg: {average_rating:.1f})')

    if command=='q':
        print('Goodbye!')
        break

