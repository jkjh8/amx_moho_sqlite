from mojo import context
import sqlite3

def create_table():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS setup (id INTEGER PRIMARY KEY, name TEXT, value TEXT)''')
    conn.commit()
    conn.close()
    
def insert_data():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("INSERT INTO setup (name, value) VALUES ('name1', 'value1')")
    conn.commit()
    conn.close()
    
def select_data():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT * FROM setup")
    rows = c.fetchall()
    conn.close()
    return rows

if __name__ == '__main__':
    create_table()
    insert_data()
    print(select_data())
    context.run(globals())
