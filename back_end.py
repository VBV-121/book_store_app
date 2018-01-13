import sqlite3

class Database:

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text,author text,year integer, book_code integer )")
        self.conn.commit()

    def insert(self,title,author,year,book_code):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,book_code))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="",author="",year="",book_code=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR book_code=?",(title,author,year,book_code))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,title,author,year,book_code):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?,book_code=? WHERE id=?",(title,author,year,book_code,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

#connect()
#update(3,"the moon","fsdfds",1845,46545)
#insert("the sun","john tablet",1984,789456123)
#print(view())
#print(search(year="1984"))
#delete(1)
