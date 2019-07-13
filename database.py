from cs50 import SQL
db = SQL("sqlite:///P2P.db")
db.execute("CREATE TABLE users(name VARCHAR(30), id VARCHAR(20) PRIMARY KEY, password VARCHAR(20),cpassword VARCHAR(20), tou VARCHAR(1), email VARCHAR(30),phone VARCHAR(10),aadhar VARCHAR(12),pan VARCHAR(10),dob VARCHAR(10),acc VARCHAR(20),ifsc VARCHAR(20))")
# db.execute("INSERT INTO login VALUES(1, 'ansh', '2299')")
# db.execute("INSERT INTO login VALUES(2, 'kd', '1234')")
# db.execute("INSERT INTO login VALUES(3, 'anay', 'khator')")
# rows = db.execute("SELECT * FROM login")
# for row in rows:
#     print(row)
