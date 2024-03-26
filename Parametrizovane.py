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
cursor.execute("SELECT * FROM books WHERE publication_year > %s AND publication_year < %s", (1900, 1950))
knihy = cursor.fetchall()
print(knihy)
