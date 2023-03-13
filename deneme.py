import _sqlite3

conneciton = _sqlite3.connect("deneme.db")

# CREATE TABLE
conneciton.execute(''' 
    create table if not exists kullanicilar
    (id integer primary key,
    isim text,
    soyad text,
    telefon_no text)

''')

# INSERT
# conneciton.execute("insert into kullanicilar (isim,soyad,telefon_no) values (?,?,?)",
#             ("ali","zeki","123")
#             )
# conneciton.execute("insert into kullanicilar (isim,soyad,telefon_no) values (?,?,?)",
#             ("veli","kavlak","456")
#             )

# SELECT
cursor = conneciton.execute("select * from kullanicilar")
# print(type(cursor))

# for deger in cursor:
#     print("id:",deger[0],
#           "isim:",deger[1],
#           "soyad:",deger[2],
#           "telefon no:",deger[3])
#     print("--------------")

# UPDATE
# conneciton.execute("update kullanicilar set telefon_no=? where id=?", ("777",3))
# conneciton.execute("update kullanicilar set telefon_no='777' where id='4'")

# DELETE
# conneciton.execute("delete from kullanicilar where id='3'")
# conneciton.execute("delete from kullanicilar where id=?", (3,))

conneciton.commit()
conneciton.close()
