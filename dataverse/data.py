import database.db as database

def create(cursor):
    try:
        cursor.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
        cursor.execute("INSERT INTO test(id, num, data) VALUES(1, 1, 'rogerio');")
        data = cursor.execute("SELECT * FROM test;")
        data = cursor.fetchall();
        for d in data:
            print("ID = ", d[0])
            print("NUMBER = ", d[1])
            print("NAME  = ", d[2], "\n")
    except:
        print("I can't access test database!")

conn = database.connect()

if conn == None:
    print("Error while connect to database")
else:
    cur = conn.cursor()
    create(cur)
