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

with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password) as conn:
    with conn.cursor() as cursor:

        # check if author exists
        lista = []

        check_auth_id = cursor.execute(
            f"SELECT authID FROM {authTable} WHERE FirstName = 'Is' and LastName = 'Asiv'",
        )
        lista = [row[0] for row in cursor]
        print(lista)
