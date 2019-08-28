import psycopg2

user = "postgres"

try:

    connect_str = "dbname='fidelis' user='postgres' host='localhost' password='iroshana1995'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()

    # create table-----------------------

    create_table_query = '''CREATE TABLE test_category
           (id INT PRIMARY KEY     NOT NULL,
           name           TEXT    NOT NULL,
           description         REAL); '''
    # cursor.execute(create_table_query)
    # conn.commit()
    # print("Table created successfully in PostgreSQL ")
# ------------------------------------------------------------
#     insert data
    sql_insert_query = """INSERT INTO test_category (id,name,description) VALUES(%s,%s,%s)"""
    record_to_insert = (5, "The Fab", "Restaurant")
    # save
    cursor.execute(sql_insert_query, record_to_insert)
    conn.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into test table")

    # print(conn.get_dsn_parameters(), "\n")
    #     #
    #     # cursor.execute("SELECT version();")
    #     # record = cursor.fetchone()
    #     # print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    # print("Error while creating PostgreSQL table", error)
    if (conn):
        print("Failed to insert record into mobile table", error)
finally:
    if (conn):
        cursor.close()
        conn.close()
        print("PostgreSQL connection is closed")
