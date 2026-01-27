movie = input("Enter the name of your 3 favorite movies (separated by commas): ")
movie_list = movie.split(",")
print(movie_list)

#2nd way
movies = []
movies.append(input("Enter the name of your 1st favorite movie: "))
movies.append(input("Enter the name of your 2nd favorite movie: "))
movies.append(input("Enter the name of your 3rd favorite movie: ")) 
print(movies)