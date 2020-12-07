import numpy as np
import pandas as pd
from sql_interaction import add_book
from database_render import render_table, render_research
from sql_interaction import get_auth_full, get_titles, get_genres
import sys

print("\n WELCOME TO YOUR HOME LIBRARY!")
while True:

    print("\n waiting for action... \n")

    print(" [ 1 ] - Add Book")

    print(" [ 2 ] - Show Database")

    print(" [ 3 ] - Search Book")

    action = input("\n select action: ")

    if action == "1":
        add_book()

    if action == "2":
        print(render_table())

    if action == "3":
        keyword = input(" Input keyword:")
        print("\n", render_research(keyword))

    else:
        sys.exit(" Exit Home Library")
