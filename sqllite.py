import sqlite3
import os

class SQLITE_UTILS:
    def __init__(self):
        try:
            self.conn = sqlite3.connect(os.path.join(os.getcwd(), 'ToDoList.db'))
            self.cursor = self.conn.cursor()
            self._verify_tables()

        except Exception as e:
            print('Error in SQLITE UTILS: ', str(e))

    def _open_conn(self):
        try:
            self.conn = sqlite3.connect(os.path.join(os.getcwd(), 'ToDoList.db'))
        except:
            pass

    def _close_conn(self):
        try:
            self.conn.close()
        except:
            pass

    def _verify_tables(self):
        self._open_conn()

        self.conn.execute('''
            CREATE TABLE  IF NOT EXISTS  ITEMS_DATA(
                NAME TEXT,
                ID NUMERIC,
                CHECKED NUMERIC
            );
        ''')

        self._close_conn()

    def insertData(self, data : list):
        self._open_conn()
        sql = f"""
            INSERT INTO ITEMS_DATA (NAME, ID, CHECKED)
            VALUES {data}
        """

        self.conn.execute(sql)
        self.conn.commit()
        self._close_conn()
        print("INSERTED")

    def readData(self):
        self._open_conn()
        sql = "SELECT NAME, ID, CHECKED from ITEMS_DATA"

        res = self.conn.execute(sql)
        res = res.fetchall()
        self._close_conn()
        return res  


    def updateChecked(self, name,id,new_check):
        self._open_conn()

        sql = f"UPDATE ITEMS_DATA SET CHECKED = {new_check} WHERE NAME = '{name}' AND ID = '{id}'"

        self.conn.execute(sql)
        self.conn.commit()
        self._close_conn()
        print('UPDATED')

    def deleteData(self, id):
        self._open_conn()

        sql = f"DELETE from ITEMS_DATA WHERE ID = '{id}'"

        self.conn.execute(sql)
        self.conn.commit()
        self._close_conn()
        print("DELETED")

    

