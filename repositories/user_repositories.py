from core.database import get_connection
from models.user import User

class UserRepository:
    def create_user(self, user:User) -> None:
        conn = get_connection()
        cursor = conn.cursor()

        sql_query = "INSERT INTO users (first_name, last_name, email) VALUES (?, ?, ?)"

        cursor.execute(sql_query, (user.first_name, user.last_name, user.email))

        conn.commit()
        conn.close()

    def find_user(self, email:str):
        conn = get_connection()
        cursor = conn.cursor()

        sql_query = "SELECT first_name, last_name, email FROM users WHERE email = ?"

        cursor.execute(sql_query, (email,))

        row = cursor.fetchone()
        conn.close()

        if row:
            return User(first_name=row[0], last_name=row[1], email=row[2])

        return None