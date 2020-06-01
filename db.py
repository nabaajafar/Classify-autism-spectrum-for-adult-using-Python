import sqlite3


conn=sqlite3.connect("DBMAs.db")
#conn.row_factory = sqlite3.Row
#db=conn.cursor()
#c.execute("CREATE TABLE IF NOT EXISTS child(fusernamd	text NOT NULL, name	text NOT NULL, age	numeric NOT NULL, result text, FOREIGN KEY(fusernamd) REFERENCES user(usename))")
#db.execute("""INSERT INTO user(username, password, email, rel) VALUES ('ba','1234', 'emaaa', 'fat')""")
#db.execute("""INSERT INTO user(username, password, email, rel) VALUES ('nametext','passwordtext', 'emailtext', 'relationtext')""")
#conn.commit()
# try:
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS user(username text PRIMARY KEY, password TEXT, email TEXT, rel TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS child(fusernamd	text NOT NULL, name	text NOT NULL, age	numeric NOT NULL, result text, FOREIGN KEY(fusernamd) REFERENCES user(usename))")
c.close()

#except Error as e:
#     print(e)



