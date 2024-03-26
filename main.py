import psycopg2
from Author import Author
conn = psycopg2.connect(
    dbname = "bnuedpct9qcua81ejilc",
    host = "bnuedpct9qcua81ejilc-postgresql.services.clever-cloud.com",
    user = "uphu5cktegkurlks01fn",
    password = "8npUda12zKCJY0tDmdRki1ed0aiHVD",
    port = "50013"
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM authors")
autori = cursor.fetchall()
print(autori)

cursor.execute("SELECT * FROM authors ORDER BY name ASC;")
prvy_autor = cursor.fetchone()
print(prvy_autor)

cursor.close()
conn.close()


# Example tuple that represents an author
author_tuple = prvy_autor

# Transform the tuple into an Author object using the imported Author class
author_object = Author(author_tuple[0],  author_tuple[1], author_tuple[2])
vsetci = autori
for i in vsetci:
    author_tuple = i
    author_object = Author(author_tuple[0],  author_tuple[1], author_tuple[2])
    print(author_object)


# Print the Author object to see the result
print(author_object)

