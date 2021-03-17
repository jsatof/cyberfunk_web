import psycopg2
import config

def create_tables(connection): # assuming connection is working

    # append commands when want to create more tables on init
    commands = (
        """
        CREATE TABLE users (
            uid SERIAL PRIMARY KEY,
            username VARCHAR(16) NOT NULL,
            password VARCHAR(16) NOT NULL
        )
        """)

    

    try:
        params = config()

        cursor = connection.cursor()

        for command in commands:
            cursor.execute(command)

        cursor.close()
        connection.commit()
    
    except(Exception. psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()

if __name__ == "__main__":
    create_tables()
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


