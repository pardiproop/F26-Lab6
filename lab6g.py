# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 11/06/2026
# Purpose: Use Dictionary for Structured Data.
# Usage: ./lab6g.py

# TO DO 1: Create function add_movie(). 
# TO DO 2: Call the function 4 times.
# TO DO 3: Print the database as instructed in readme.md file.
# TO DO 4: Run the script. Take screenshot of code and script.
def add_movie(database,name,director,year,runtime):
    movie={"name":name,"director":director,"year":year,"runtime":runtime}
    database.append(movie)

def main():
    movie_database=[]
    add_movie(movie_database,"Tatanic","James Cameron",1997,195)
    add_movie(movie_database,"Avengers Infinity War","Russo Brothers",2018,149)
    add_movie(movie_database,"Shawshank Redemption","Frank Darabont",1994,142)
    add_movie(movie_database,"1917","Sam Mendes",2019,119)
    add_movie(movie_database,"Odyssey","Christopher Nolan",2026,173)
    for movie in movie_database:
        print(movie)
main()
