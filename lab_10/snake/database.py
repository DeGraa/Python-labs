import psycopg2
from config import load_config


def insert_user(username, score, level):
    sql = """INSERT INTO users(username, score, level) VALUES(%s, %s, %s);"""
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (username, score, level))
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def get_data():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT username, score, level FROM users ORDER BY score")
                rows = cur.fetchall()

                print("The number of users: ", cur.rowcount)
                for row in rows:
                    print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
