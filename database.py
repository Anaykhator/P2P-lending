from cs50 import SQL
db = SQL("sqlite:///P2P.db")
db.execute("CREATE TABLE users(name VARCHAR(30), id VARCHAR(20) PRIMARY KEY, password VARCHAR(20), tou VARCHAR(1), email VARCHAR(30),phone VARCHAR(10),aadhar VARCHAR(12),pan VARCHAR(10),dob VARCHAR(10),acc VARCHAR(20),ifsc VARCHAR(20))")
db.execute("CREATE TABLE requests(requestid INTEGER PRIMARY KEY AUTOINCREMENT, borid VARCHAR(20),tenure INT, amt INT, borscore FLOAT, borname VARCHAR(30),loantype VARCHAR(20),FOREIGN KEY (borname) REFERENCES users(name),FOREIGN KEY (borid) REFERENCES users(id))")
# db.execute("DROP TABLE proposals")
db.execute("CREATE TABLE proposals(lenid VARCHAR (20),reqid VARCHAR (20),roi int , percentageofloan INT,FOREIGN KEY (reqid) REFERENCES requests(requestid),FOREIGN KEY (lenid) references users(id))")
db.execute("CREATE TABLE transactions(lenid VARCHAR(20),borrid VARCHAR(20),tranid INTEGER PRIMARY KEY AUTOINCREMENT,amt int,tenure INT,type VARCHAR(1),succ VARCHAR(1),loanid INTEGER,roi INT,FOREIGN KEY (loanid) references requests(requestid),FOREIGN KEY (lenid) references users(id),FOREIGN KEY (borrid) references requests(borid),FOREIGN KEY (roi) REFERENCES proposals(roi))")


