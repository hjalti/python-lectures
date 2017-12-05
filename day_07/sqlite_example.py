import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute('''CREATE TABLE songs
    (title text, artist text, duration integer)''')

c.execute('''INSERT INTO songs VALUES
    ('Oops!... I did it again', 'Britney Spears', 180)''')
c.execute('''INSERT INTO songs VALUES
    ('Crazy', 'Britney Spears', 240)''')
c.execute('''INSERT INTO songs VALUES
    ('If I had a million dollars', 'Barenaked ladies', 120)''')

conn.commit()

c = conn.cursor()

for row in c.execute('SELECT * FROM songs WHERE artist=?', ('Britney Spears',)):
    print(row)


conn.close()
