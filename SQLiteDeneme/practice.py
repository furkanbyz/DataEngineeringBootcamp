import sqlite3

connection=sqlite3.connect("fenerbahce.db")
connection.execute("create table if not exists players(id integer primary key, name text, surname text, number text)")

# INSERT
# connection.execute("insert into players (name, surname, number) values(?,?,?)",
#                    ("enner","valencia","9")
#                    )
# connection.execute("insert into players (name, surname, number) values(?,?,?)", 
#                    ("joshua","king","20")
#                    )

# ALTER
# connection.execute("alter table players add column goals text")

# DELETE
# connection.execute("delete from players where name='enner'")

# SELECT
# all = connection.execute("select * from players")
# for i in all:
#     print(i[1])
# for i in all:
#     print("id:",i[0],
#           "name:",i[1],
#           "surname:",i[2],
#           "shirt number:",i[3],
#           "number of goals:",i[4])
#     print("-------------------")

connection.commit()
connection.close()