import psycopg2

from database_package.database import Con

conn = psycopg2.connect(
    host="92.53.115.42",
    database="default_db",
    user="gen_user",
    password="Wedontneednoeducation"
)

conn.autocommit = True
cursor = conn.cursor()
# query = "CREATE TABLE mishabot " \
#         "( chat_id     text, " \
#         "number      text," \
#         "lasttext    text," \
#         "googleforms text," \
#         "diete       text," \
#         "date        text," \
#         "approved    text," \
#         "payment     text," \
#         "exception   integer," \
#         "plus        text," \
#         "balance     integer," \
#         "tariff      integer" \
#         ");"
# cursor.execute(query)

# query = "INSERT INTO mishabot " \
#         "VALUES" \
#         "('943532917','79266390551','присед','1p9qEu3zVfYG-NB7dQZbpKV75Gv6Dao0oVkE7f9AFTT0','воды пей' ,6,'yes',null,11111,'required',3,2)"
# cursor.execute(query)
#
#
query = "SELECT * FROM mishabot"

cursor.execute(query)
print(cursor.fetchall())