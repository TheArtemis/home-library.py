import pandas as pd
import pyodbc

server = "DESKTOP-HCJ19NU\SQLEXPRESS"
database = "HomeLibraryDB"

username = "access"
password = "access1"
driver = '{ODBC Driver 17 for SQL Server}'

# Tables

booksTable = "dbo.Books"
authTable = "dbo.Author"
genreTable = "dbo.Genre"

"""
with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
    with conn.cursor() as cursor:

        sql_query = pd.read_sql_query(
            'SELECT TOP(1000)[bookID], [bookName], [bookAuthor], [bookGenre] FROM[HomeLibraryDB].[dbo].[Books]', conn)

        print(sql_query)
"""
# DESKTOP-HCJ19NU\SQLEXPRESS

# HomeLibraryDB

# dbo.Books


def check_auth(auth_fn: str, auth_ln: str) -> list:
    with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
        with conn.cursor() as cursor:

            cursor.execute(
                f"SELECT authID FROM {authTable} where FirstName = '{auth_fn}' and LastName = '{auth_ln}'"
            )

            temp = [row[0] for row in cursor]

            return temp


def insert_auth(auth_fn: str, auth_ln: str):

    with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
        with conn.cursor() as cursor:

            cursor.execute(
                f"insert into {authTable} (LastName, FirstName) values ('{auth_ln}','{auth_fn}')"
            )

            conn.commit()
            return print(f"{auth_fn} {auth_ln} was added to Authors Table")


def check_genr(genre: str):

    with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"select genrID from {genreTable} where Genre = '{genre}'"
            )

            temp = [row[0] for row in cursor]

            return temp


def insert_genr(genre: str):
    with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"insert into {genreTable} (Genre) values ('{genre}')"
            )

            conn.commit()

            return print(f"{genre} was added to Genres Table")


def insert_book(book: str, authID: int, genrID: int):
    with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"insert into {booksTable} (bookName, bookAuthor, bookGenre) values ('{book}', '{authID}', '{genrID}')"
            )
            conn.commit()
            return print(f"{book} è stato inserito correttamente nella Home Library")


def add_book():
    # initialize
    book_name = input("Book Name: ")
    add_author = input("Insert Author Name: ")
    add_genres = input("Insert one or more Genres: ")

    # prepare author first and last name
    author_first_name = add_author.split(" ")[0]
    author_last_name = add_author.split(" ")[1]

    # split the input genres into a list
    genres_list = add_genres.split(" ")

    # check if author exists

    auth = check_auth(author_first_name, author_last_name)

    if auth != []:
        authID = auth[0]

    else:
        insert_auth(author_first_name, author_last_name)
        auth = check_auth(author_first_name, author_last_name)
        authID = auth[0]

    # checks if genres exists

    # MUST BE CORRECTED FOR MULTIPLE GENRES ADD, NOW IT ONLY TAKES ONE
    genr = check_genr(genres_list[0])

    if genr != []:
        genrID = genr[0]

    else:
        insert_genr(genres_list[0])
        genr = check_genr(genres_list[0])
        genrID = genr[0]

    # inserisce dati dentro books table

    insert_book(book_name, authID, genrID)


def get_auth_full():
    with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
        with conn.cursor() as cursor:

            cursor.execute(
                f"select FirstName from {authTable}"
            )

            first_names = [row for row in cursor]

            cursor.execute(
                f"select LastName from {authTable}"
            )

            last_names = [row[0] for row in cursor]

            full_names = [elem[0] + " " + item for elem,
                          item in zip(first_names, last_names)]

            return full_names


def get_titles():
    with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
        with conn.cursor() as cursor:

            cursor.execute(
                f"select bookName from {booksTable}"
            )

            book_titles = [row[0] for row in cursor]

            return book_titles


def get_genres():
    with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
        with conn.cursor() as cursor:

            cursor.execute(
                f"select Genre from {genreTable}"
            )

            genres = [row[0] for row in cursor]

            return genres


def make_table():

    with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
        with conn.cursor() as cursor:

            display_titles = get_titles()

            cursor.execute(
                f"select bookAuthor from {booksTable}"
            )

            author_ids = [row[0] for row in cursor]

            auth_first_names = []

            auth_last_names = []

            for elem in author_ids:
                cursor.execute(
                    f"select FirstName from {authTable} where authID = {elem}"
                )
                for row in cursor:
                    auth_first_names.append(row[0])

                cursor.execute(
                    f"select LastName from {authTable} where authID = {elem}"
                )
                for row in cursor:
                    auth_last_names.append(row[0])

            display_authors = []

            display_genres = []

            for item1, item2 in zip(auth_first_names, auth_last_names):
                display_authors.append(item1+" "+item2)

            cursor.execute(
                f"select bookGenre from {booksTable}"
            )

            genr_ids = [row[0] for row in cursor]

            for item in genr_ids:
                cursor.execute(
                    f"select Genre from {genreTable} where genrID = {item}"
                )
                for row in cursor:
                    display_genres.append(row[0])

            return display_titles, display_authors, display_genres
