import numpy as np
import pandas as pd
from sql_interaction import add_book
from database_render import render_table
import sys

print("\n WELCOME TO YOUR HOME LIBRARY!")
while True:

    print("\n waiting for action... :\n")

    print(" [ 1 ] - Add Book")

    print(" [ 2 ] - Show Database")

    action = input("\n select action: ")

    if str(action) == "1":
        add_book()

    if str(action) == "2":
        print(render_table())
    else:
        sys.exit(" Exit Home Library")
