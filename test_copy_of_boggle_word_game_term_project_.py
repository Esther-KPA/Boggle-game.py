# -*- coding: utf-8 -*-
#Test-Copy of Boggle/word game - Term project .ipynb

#Automatically generated by Colaboratory.

#Original file is located at
    #https://colab.research.google.com/drive/16u21SwF1ZJ6FXgwC5lqGyMnd-BIti0-P

#Generate a 4x4 board that consists of random letters. Use ‘random’ and ‘string’e libraries.


# Importing random module that provides functions to generate random numbers and
# string module that provides a collection of string-related functions.

import random
import string

# Function that generates a random letter uppercase letter, returning this randomly
# chosen letter
def generate_random_letter():
  return random.choice(string.ascii_uppercase)

#Creates a 4 by 4 board with random letters
def create_random_board(rows, cols):
  board = []
  for _ in range(rows):
    row =[generate_random_letter() for _ in range(cols)]
    board.append(row)
  return board

# A function that prints the board
def print_board(board):
  for row in board:
    print(" ".join(row))

# Generates and prints the random 4 by 4 board.
random_board = create_random_board(4, 4)
print_board(random_board)# In final code, we do not need this step

#Ask user to find all valid English words (3 or more characters) vertically (top-down, down-top) or horizontally (left-right, right-left).

# Defining a function to find valid words in rows of a board, as it iterates through
# each row on board, it joins the letters into a single string
def find_valid_words_in_rows(board):
  words = []
  for row in board:
    word = "".join(row)
    words.extend(find_valid_words(word))
    return words

# Defining a function to find valid words in columns of a board, as it iterates through
# each column on board, it joins the letters into a single string
def find_valid_words_in_columns(board):
  words = []
  for col in range(len(board[0])):
    word = "".join(board[row][col] for row in range(len(board)))
    words.extend(find_valid_words(word))
    return words

# The find_valid_words function takes word as input, iterates through to find all possible
# substrings and if it is valid in english dictionary. Each word length would have to be
# greater than or equal to 3
def find_valid_words(word):
  valid_words = []
  for i in range(len(word)):
      for j in range(i + 2, len(word) +1):
          substring = word[i:j]
      if len(substring) >= 3 and substring.lower() in english_dictionary:
        valid_words.append(substring)
  return valid_words

# Using the calculate_points function that takes word as input, calculates points based on word length
def calculate_points(word):
    return len(word)

# load a simple english dictionary
english_dictionary = set(["cat", "bat","rat", "mat", "hat", "dog", "car"])#what if these words are not
#part of the randomly generated letters?

# A random 4 by 4 board is generated using the function "create_random_board"
random_board = create_random_board(4, 4)
print_board(random_board)

#Finds valid words in rows of random board generated and prints them
row_words = find_valid_words_in_rows(random_board)
print("\nValid words in rows:", row_words) #In final code, we dont need this step

#Finds valid words in columns of random board generated and prints them
column_words = find_valid_words_in_columns(random_board)
print("\nValid words in columns:", column_words) #In final code we dont need this step

#to print all valid words in rows & columns
all_words = find_valid_words_in_rows(random_board) + find_valid_words_in_columns(random_board)
print("\nValid words in rows and columns:", all_words)

#Users might provide the answer using input function until they decide there is no words left to be found.

# game loop until no words left, starts with setting "total points" variable to zero
total_points = 0

# checks if there any words found, if not, it prints message showing this
if not all_words:
  print("No words were found. Your score is 0.")
else: #otherwise goes in a loop to keep asking the user to input a word until no more words.
   while all_words:
      user_input = input("\nEnter a word (or type 'exit' to end): ").strip().upper()
# checks if the user inputs the word "exit", a thank you message and score will pop up

      if user_input == 'EXIT':
         print("\nThank you for playing! Your final score is {total_points} points.")
         break
# checking if the input word is valid as in "all_words" list, if true, it calculates
# using the "calculate_points function"
      if user_input in all_words:
        points = calculate_points(user_input)
        total_points += points
        print(f"Great! '{user_input}' is a valid word. Your earned {points} points. Total points: {total_points}")
        all_words.remove(user_input)
      else:
        print(f"sorry, '{user_input}' is not an existing word or has already been found.Give it another go.")



