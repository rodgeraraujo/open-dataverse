import psycopg2

try:
    conn = psycopg2.connect(
        user = "postgres",
        password = "secret",
        host = "127.0.0.1",
        port = "5432",
        database = "dataverse"
    )

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

cur = conn.cursor()

try:
    cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
    cur.execute("INSERT INTO test(id, num, data) VALUES(1, 1, 'rogerio');")
    data = cur.execute("SELECT * FROM test;")
    data = cur.fetchall();
    for d in data:
        print("ID = ", d[0])
        print("NUMBER = ", d[1])
        print("NAME  = ", d[2], "\n")
except:
    print("I can't access test database!")