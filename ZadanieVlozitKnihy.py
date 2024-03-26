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
title = "Pan prstenov spolocenstvo prstena"
author_id = "Gallik"
genre_id = 1
ISBN = "978E80E556E0634E7"
publication_year = 1954
copies = 4
name = "J.R.R. Tolkien"
bio = "Vyborny autor fantasy 20. storocia"
# cursor.execute("SELECT books.title FROM books INNER JOIN genres ON books.genre_id = genres.genre_id")
# cursor.execute("SELECT * FROM books WHERE genre_ID = %s AND publication_year < %s", (1900, 1950))
# cursor.execute("SELECT b.title, g.name from books b INNER JOIN genres g on g.genre_id = b.genre_id where g.name = %s", ('Fantasy',))
# cursor.execute("SELECT b.title, g.name from books b INNER JOIN genres g on g.genre_id = b.genre_id where g.name = %s", (vybrany,))
# print(cursor.fetchall())
# cursor.execute("""INSERT INTO books (title, author_id, genre_id, ISBN, publication_year, copies)
# VALUES (%s, %s, %s, %s, %s, %s,)""", (title, author_id, genre_id, ISBN, publication_year, copies))
# conn.commit()
cursor.execute("""INSERT INTO authors (name, bio)
VALUES (%s, %s)
""", (name, bio))
conn.commit()
print("Novy autor bol pridany")
cursor.close()
