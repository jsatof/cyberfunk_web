import psycopg2

def user_lookup(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT uid, username, password FROM users ORDER BY uid"

        cursor.execute(query)

        matches = []        

        row = cursor.fetchone()

        cursor.close()



    except(Exception, psycopg2.DatabaseError) as error:
        print(error)


