import numpy as np
import pandas as pd
from sql_interaction import add_book
from database_actions import show_database

from sql_interaction import get_auth_full, get_titles, get_genres

print("\n WELCOME TO YOUR HOME LIBRARY!")

print("\n Select Action:\n")

print(" [ 1 ] - Add Book")

print(" [ 2 ] - Show Database")

action = input("\n input number: ")

if int(action) == 1:
    add_book()

if int(action) == 2:
    print("", get_auth_full(), "\n", get_titles(), "\n", get_genres(), "\n")
