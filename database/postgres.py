import psycopg2
from dotenv import load_dotenv
import os

class PostgresDB:
    
    
    def __init__(self):
        HOSTDB = os.getenv("host_db")
        DATABASE = os.getenv("database")
        USERDB = os.getenv("user_db")
        PASSWORD = os.getenv("password_db")
        try:
            self.connection = psycopg2.connect(
                host="postgresql",
                database="todolegaldb",
                user="usertl",
                password="12345678",
                port="5432"
            )
            self.cursor = self.connection.cursor()
        except (Exception, psycopg2.Error) as error:
            print("Error al conectar a PostgreSQL:", error)
            self.connection = None
            self.cursor = None

    def execute(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            column_names = [desc[0] for desc in self.cursor.description]
            result = []
            rows = self.cursor.fetchall()
            for row in rows:
                row_dict = dict(zip(column_names, row))
                result.append(row_dict)
                
            return result
        except (Exception, psycopg2.Error) as error:
            print("Error al ejecutar la consulta:", error)
            return None
    
    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        
    
    