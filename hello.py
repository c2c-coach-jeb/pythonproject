import sqlite3

con = sqlite3.connect("banking_app.sqlite")

# print("Creating table")
# con.execute("""create table users (
#   id integer,
#   lastname TEXT,
#   firstname TEXT,
#   email TEXT
# )""")

# con.execute(
#     "insert into users (id, lastname, firstname, email) values (1, 'McCartney', 'Paul', 'paul@thebeatles.com')"
# )
# con.commit()
cur = con.execute("select * from users")
print(cur.fetchone())
