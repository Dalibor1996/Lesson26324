import psycopg2
from Author import Author
conn = psycopg2.connect(
    dbname = "bnuedpct9qcua81ejilc",
    host = "bnuedpct9qcua81ejilc-postgresql.services.clever-cloud.com",
    user = "uphu5cktegkurlks01fn",
    password = "8npUda12zKCJY0tDmdRki1ed0aiHVD",
    port = "50013"
)
# vybrany = str(input("Napis co chces najst "))
cursor = conn.cursor()
first_name = "Dalibor"
last_name = "Gallik"
email = "dalibor1910@gmail.com"
# cursor.execute("SELECT books.title FROM books INNER JOIN genres ON books.genre_id = genres.genre_id")
# cursor.execute("SELECT * FROM books WHERE genre_ID = %s AND publication_year < %s", (1900, 1950))
# cursor.execute("SELECT b.title, g.name from books b INNER JOIN genres g on g.genre_id = b.genre_id where g.name = %s", ('Fantasy',))
# cursor.execute("SELECT b.title, g.name from books b INNER JOIN genres g on g.genre_id = b.genre_id where g.name = %s", (vybrany,))
# print(cursor.fetchall())
cursor.execute("""INSERT INTO members (first_name, last_name, email)
VALUES (%s, %s, %s)""", (first_name, last_name, email))
conn.commit()
print("Novy clen bol pridany")
cursor.close()
