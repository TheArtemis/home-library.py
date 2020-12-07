import pyodbc
import numpy as np
import pandas as pd
from sql_interaction import make_table

server = "DESKTOP-HCJ19NU\SQLEXPRESS"
database = "HomeLibraryDB"

username = "access"
password = "access1"
driver = '{ODBC Driver 17 for SQL Server}'

# Tables

booksTable = "dbo.Books"
authTable = "dbo.Author"
genreTable = "dbo.Genre"


def render_table():
    table = make_table()
    data = {"Title": table[0],
            "Author": table[1],
            "Genre": table[2]}

    data_frame = pd.DataFrame(data, columns=["Title", "Author", "Genre"])

    return data_frame
