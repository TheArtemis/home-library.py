import pandas as pd
from sql_interaction import get_auth_full, get_titles, get_genres


class Book:
    def __init__(self):
        self.title = get_titles()
        self.author = get_auth_full()
        self.genre = get_genres()

    def count_titles(self):
        return titles.count
