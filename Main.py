import numpy as np
import pandas as pd
from sql_interaction import add_book
from database_render import render_table, render_research
from sql_interaction import get_auth_full, get_titles, get_genres, get_auth, check_book
import sys

print("\n WELCOME TO YOUR HOME LIBRARY!")
while True:

    print("\n waiting for action... \n")

    print(" [ 1 ] - Add Book")

    print(" [ 2 ] - Show Database")

    print(" [ 3 ] - Search Book")

    print(" [ 4 ] - Check if book in database")

    action = input("\n select action: ")

    if action == "1":
        add_book()

    elif action == "2":
        print(render_table())

    elif action == "3":
        keyword = input(" Input keyword:")
        print("\n", render_research(keyword))

    elif action == "4":
        keyword = input(" Input book to check:")
        print("\n", check_book(keyword))

    else:
        sys.exit(" Exit Home Library")
