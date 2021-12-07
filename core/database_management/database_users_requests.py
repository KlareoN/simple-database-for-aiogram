from sqlite3 import connect

class database_users_req:
    __DB_LOCATION = 'database/users.db'

    def __init__(self):
        self.__connection = connect(self.__DB_LOCATION)
        self.__cursor = self.__connection.cursor()

    def exists_account(
        self,
        user_id: int
    ) -> bool:
        """Проверка, существует аккаунт или нет."""
        """Checking whether the account exists or not."""
        
        self.__cursor.execute(
            'SELECT user_id FROM users WHERE user_id IN (?) LIMIT 1',
            (user_id,)
        )
        if self.__cursor.fetchone() is None:
            return False
        else:
            return True

    def create_account(
        self,
        user_id: int,
    ) -> None:
        """Создание аккаунта пользователю"""
        """Creating a user account"""
        
        self.__cursor.execute(
            '''
            INSERT INTO users 
            (user_id) 
            VALUES (?)
            ''',
            (user_id,)
        )
        self.__connection.commit()

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.__cursor.close()

        if isinstance(exc_value, Exception):
            self.__connection.rollback()
        else:
            self.__connection.commit()

        self.__connection.close()

    def __del__(self):
        self.__connection.close()