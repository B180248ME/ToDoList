import sqlite3, os, sys
from datetime import datetime

class SQLITE_UTILS:
    def __init__(self):
        try:
            self.conn = sqlite3.connect(os.path.join(os.getcwd(), 'ToDoList.db'))
            self.cursor = self.conn.cursor()
            self.initiateLog(os.path.join(os.getcwd(), 'ToDoList.log'))
            self._verify_tables()

        except Exception as e:
            self.writeToLogs(f'Error in SQLITE UTILS i.e {e}','Warning')

    def initiateLog(self, filename):
        self.__logFile = filename
        self.__logFileContent = ""
        with open(self.__logFile, 'w', encoding='UTF8') as f:
            f.write(str(""))

    
    def updateLog(self, msg, level):
        dateObj = datetime.now().strftime("%d/%m/%Y %H:%M:%S") 
        msg = msg.lower().title()
        self.__logFileContent = self.__logFileContent + f'{dateObj} {level.upper()}: {msg}\n'
        print(f'\n{dateObj} {level.upper()}: {msg}')

    def flushLog(self):
        with open(self.__logFile,"w+") as LF:
            LF.write(self.__logFileContent)

    def writeToLogs(self,msg, level):
        try:
            dateObj = datetime.now().strftime("%d/%m/%Y %H:%M:%S") 
            msg = msg.lower().title()
            content = f'{dateObj} {level.upper()}: {msg}\n'
            with open(self.__logFile , 'a', encoding='UTF8') as f:
                f.write(str(content))

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('-----------------Error----------')
            print(exc_type, fname, exc_tb.tb_lineno)
            print(e)


    def _open_conn(self):
        try:
            self.conn = sqlite3.connect(os.path.join(os.getcwd(), 'ToDoList.db'))
        except Exception as e:
            self.writeToLogs(f'Error Opening Sqlite Connection i.e {e}','Warning')

    def _close_conn(self):
        try:
            self.conn.close()
        except Exception as e:
            self.writeToLogs(f'Error Closing Sqlite Connection i.e {e}','Warning')

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
        self.writeToLogs('Verified Sqlite DB Tables','Info')

    def insertData(self, data : list):
        self._open_conn()
        sql = f"""
            INSERT INTO ITEMS_DATA (NAME, ID, CHECKED)
            VALUES {data}
        """

        self.conn.execute(sql)
        self.conn.commit()
        self._close_conn()
        self.writeToLogs('Inserted into Sqlite DB ITEMS_DATA table','Info')

    def readData(self):
        self._open_conn()
        sql = "SELECT NAME, ID, CHECKED from ITEMS_DATA"

        res = self.conn.execute(sql)
        res = res.fetchall()
        self._close_conn()
        self.writeToLogs('Read Sqlite DB ITEMS_DATA table','Info')
        return res  


    def updateChecked(self, name,id,new_check):
        self._open_conn()

        sql = f"UPDATE ITEMS_DATA SET CHECKED = {new_check} WHERE NAME = '{name}' AND ID = '{id}'"

        self.conn.execute(sql)
        self.conn.commit()
        self._close_conn()
        self.writeToLogs('Updated into Sqlite DB ITEMS_DATA table','Info')

    def deleteData(self, id):
        self._open_conn()

        sql = f"DELETE from ITEMS_DATA WHERE ID = '{id}'"

        self.conn.execute(sql)
        self.conn.commit()
        self._close_conn()
        self.writeToLogs('Deleted Sqlite DB ITEMS_DATA Table Row Data','Info')

    def clearData(self):
        self._open_conn()

        sql = f"DELETE from ITEMS_DATA"

        self.conn.execute(sql)
        self.conn.commit()
        self._close_conn()
        self.writeToLogs('Deleted Sqlite DB ITEMS_DATA Table All Data','Info')

    

