import psycopg2
import csv
from config import load_config


class Database:
    def __init__(self):
        self.config = load_config()

    def create_table(self):
        command = """
        CREATE TABLE IF NOT EXISTS contacts(
            username VARCHAR(255),
            phone_number VARCHAR(255));
        """
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(command)
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)

    def insert_contact(self, username, phone_number):
        sql = """INSERT INTO contacts(username, phone_number)
             VALUES(%s, %s) RETURNING id;"""
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (username, phone_number))
                    new_id = cur.fetchone()[0]
                    conn.commit()
                    return new_id
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def update_username(self, phone_number, username):
        sql = """
        UPDATE contacts
        SET username = %s
        WHERE phone_number = %s
        """
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (username, phone_number))
                conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def delete_username(self, phone_number):
        sql = "DELETE FROM contacts WHERE phone_number = %s"
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (phone_number,))
                conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_all_contacts(self):
        sql = "SELECT username, phone_number FROM contacts ORDER BY username"
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    return cur.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return []

    def import_contacts_from_csv(self, csv_file_path):
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    with open(csv_file_path, mode="r", encoding="utf-8") as file:
                        reader = csv.reader(file)
                        next(reader)
                        for row in reader:
                            cur.execute(
                                "INSERT INTO contacts (username, phone_number) VALUES (%s, %s);",
                                (row[0], row[1]),
                            )
                    conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error importing contacts: {error}")

    def search(self, pattern):
        sql = """
        SELECT username, phone_number FROM contacts
        WHERE LOWER(username) LIKE LOWER(%s)
        OR LOWER(phone_number) LIKE LOWER(%s)
        """
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    search_pattern = f"%{pattern}%"
                    cur.execute(sql, (search_pattern, search_pattern))
                    results = cur.fetchall()
                    return results
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error searching for contacts: {error}")
            return []

    def import_contacts_from_list(self, contact_list):
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    for item in contact_list:
                        cur.execute(
                            "INSERT INTO contacts (username, phone_number) VALUES (%s, %s);",
                            (item[0], item[1]),
                        )
                conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            conn.rollback()
            print(f"Error importing contacts: {error}")

    def get_some_contacts(self, limit, offset):
        sql = "SELECT username, phone_number FROM contacts LIMIT %s OFFSET %s"
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (limit, offset))
                    return cur.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return []
