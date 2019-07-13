from cs50 import SQL
db = SQL("sqlite:///P2P.db")
db.execute("CREATE TABLE users(name VARCHAR(30), id VARCHAR(20) PRIMARY KEY, password VARCHAR(20), tou VARCHAR(2), email VARCHAR(30),)")
# db.execute("INSERT INTO login VALUES(1, 'ansh', '2299')")
# db.execute("INSERT INTO login VALUES(2, 'kd', '1234')")
# db.execute("INSERT INTO login VALUES(3, 'anay', 'khator')")
# rows = db.execute("SELECT * FROM login")
# for row in rows:
#     print(row)
