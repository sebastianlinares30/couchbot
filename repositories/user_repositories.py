from core.database import get_connection
from models.user import User

"""
This module manages database interactions for the User.
It handles operations such as creating new user records and querying existing ones by email.
"""

class UserRepository:
    def create_user(self, user:User) -> None:
        """
        Establishes a database connection and inserts a new user into the user table using values from the User object.
        """
        conn = get_connection()
        cursor = conn.cursor()

        sql_query = "INSERT INTO users (first_name, last_name, email) VALUES (?, ?, ?)"

        # Executes query
        cursor.execute(sql_query, (user.first_name, user.last_name, user.email))

        conn.commit()
        conn.close()

    def find_user(self, email:str):
        """
        Queries the database for a user matching the email address.
        Returns a User instance if found or None otherwise.
        """
        conn = get_connection()
        cursor = conn.cursor()

        sql_query = "SELECT first_name, last_name, email FROM users WHERE email = ?"

        # Passes the email string as a single-element tuple
        cursor.execute(sql_query, (email,))

        row = cursor.fetchone()
        
        conn.close()

        # If a record exists, unpack the row tuple into a new User object
        if row:
            return User(first_name=row[0], last_name=row[1], email=row[2])

        return None