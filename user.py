# from database import connect
# from database import connection_pool
from database import CursorConnectionFromPool


class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return 'User {}'.format(self.email)

    def save_to_db(self):
        with CursorConnectionFromPool() as cursor:
            # Running code
            cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)',
                           (self.email, self.first_name, self.last_name))
        # connection.commit()
        # connection_pool.putconn(connection)
        # connection.commit()
        # connection.close()

    @classmethod
    def load_from_db_by_email(cls, email):
        with CursorConnectionFromPool() as cursor:
            # connection = connection_pool.getconn()
            cursor.execute('SELECT * FROM users WHERE email=%s', (email,))
            user_data = cursor.fetchone()
            return cls(email=user_data[1], first_name=user_data[2], last_name=[3], id=user_data[0])