import pandas as pd
import pyodbc


class addBook:
    def __init__(self,
                 server="DESKTOP-HCJ19NU\SQLEXPRESS",
                 database="HomeLibraryDB",
                 username="access",
                 password="access1",
                 driver='{ODBC Driver 17 for SQL Server}',
                 booksTable="dbo.Books",
                 authTable="dbo.Author",
                 genreTable="dbo.Genre"):

        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.driver = driver
        self.booksTable = booksTable
        self.authTable = authTable
        self.genreTable = genreTable

    def check_auth(self, auth_fn: str, auth_ln: str) -> list:
        with pyodbc.connect('DRIVER='+self.driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
            with conn.cursor() as cursor:

                cursor.execute(
                    f"SELECT authID FROM {authTable} where FirstName = '{auth_fn}' and LastName = '{auth_ln}'"
                )

                temp = [row[0] for row in cursor]

                return temp

    def insert_auth(self, auth_fn: str, auth_ln: str):

        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
            with conn.cursor() as cursor:

                cursor.execute(
                    f"insert into {authTable} (LastName, FirstName) values ('{auth_ln}','{auth_fn}')"
                )

                conn.commit()
                return print(f"{auth_fn} {auth_ln} was added to Authors Table")

    def check_genr(self, genre: str):

        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    f"select genrID from {genreTable} where Genre = '{genre}'"
                )

                temp = [row[0] for row in cursor]

                return temp

    def insert_genr(self, genre: str):
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    f"insert into {genreTable} (Genre) values ('{genre}')"
                )

                conn.commit()

                return print(f"{genre} was added to Genres Table")

    def insert_book(self, book: str, authID: int, genrID: int):
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    f"insert into {booksTable} (bookName, bookAuthor, bookGenre) values ('{book}', '{authID}', '{genrID}')"
                )
                conn.commit()
                return print(f"{book} è stato inserito correttamente nella Home Library")

    def book_inputs():
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
