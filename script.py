import string
from textwrap import TextWrapper, dedent
from dataGather import *
from linkedlist import *
from welcome import *


# FUNCTIONS
# Function to determine if user wants to search by genre or alphabet

def get_search_on():
    search_by = ''
    while len(search_by) == 0:
        user_input = str(input("\n\n How would you like to search for movies? \nType g for genre, a for alphabetical\n")).lower()
        if user_input != 'g' and user_input != 'a':
            print('\n That is not a valid response. Please try again.')
        else:
            search_by = 'genre' if user_input == 'g' else ('rating' if user_input == 'r' else 'letter')
    return search_by

# Create a code to insert genres into a data structure like LinkedList 
# for searching by genre

def insert_genre_types():
    genre_list = LinkedList()
    for genre in genres:
        genre_list.insert_beginning(genre)
    return genre_list

# for searching alphabetically

def insert_alphabet():
    alphabet_list = LinkedList()
    for letter in string.ascii_uppercase:
        alphabet_list.insert_beginning(letter, 0)
    return alphabet_list

# Create a code to insert movies into a data structure like LinkedList
# sorting by genre

def insert_movie_data_genre():
    movie_data_list = LinkedList()
    remove_list = []
    for genre in genres:
        genre_sublist = LinkedList()
        for movie in movies:
            index = 0
            while index < len(movie[0]):
                if movie[0][index] == genre:
                    movie_this_genre = [genre] + movie
                    genre_sublist.insert_beginning(movie_this_genre, 2)
                index += 1
        if genre_sublist.get_head_node().get_value() != None:
            movie_data_list.insert_beginning(genre_sublist)
        else:
            remove_list.append(genre)
    return movie_data_list, remove_list
        
