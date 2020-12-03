import pyodbc
import numpy as np
import pandas as pd

server = "DESKTOP-HCJ19NU\SQLEXPRESS"
database = "HomeLibraryDB"

username = "access"
password = "access1"
driver = '{ODBC Driver 17 for SQL Server}'

# Tables

booksTable = "dbo.Books"
authTable = "dbo.Author"
genreTable = "dbo.Genre"


def show_database():
    with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
        sql_query = pd.read_sql_query(
            'SELECT TOP(1000)[bookID], [bookName], [bookAuthor], [bookGenre] FROM[HomeLibraryDB].[dbo].[Books]', conn)

        print(sql_query)
