import sqlite3


class CRUD:

    def __init__(self, name):
        self.conn = sqlite3.connect(f"{name}.db")
        self.cursor = self.conn.cursor()

    def CreateDB(self, name):
        self.cursor.execute(f"CREATE DATABASE {name}")
        self.conn.commit()

    def CreateTable(self, name, fields):
        self.cursor.execute(f"CREATE TABLE {name} ({fields})")
        self.conn.commit()

    def Insert(self, name, fields, data):
        try:
            self.cursor.execute(f"INSERT INTO '{name}'({fields}) VALUES ({data})")
            self.conn.commit()
            return 1
        except sqlite3.IntegrityError as e:
            return e.sqlite_errorcode
        except sqlite3.OperationalError:
            return 0

    def Read(self, name, fields, parameters=1):
        try:
            self.cursor.execute(f" SELECT {fields} FROM {name} WHERE {parameters}")
            return self.cursor.fetchall()
        except sqlite3.OperationalError as e:
            print(e)
            return 0

    def Update(self, name, field, parameters=1):
        try:
            self.cursor.execute(f"UPDATE {name} SET {field} WHERE {parameters}")
            self.conn.commit()
            return 1
        except sqlite3.OperationalError as e:
            print(e)
            return 0

    def Delete(self, name, parameters=1):
        self.cursor.execute(f"DELETE FROM {name} WHERE {parameters}")
        self.conn.commit()

    def Close(self):
        self.conn.close()


