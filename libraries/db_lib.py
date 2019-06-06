from static.db_credentials import credentials
import mysql.connector as mariadb

print(credentials)

class db_handler():

    def __init__(self, name=credentials['user'], passwd=credentials['passwd']):
        self.user = name
        self.passwd = passwd
        #self.host = host

    def connect(self):

        self._db_conn=mariadb.connect(user=self.user,passwd=self.passwd)
        self._db_cur = self._db_conn.cursor()

    def close_conn(self):
        self._db_conn.close()

    def create_db(self, name):
        self._db_cur.execute('create database if not exists %s;' % name)
        self._db_conn.commit()

    def use_db(self, name):
        self._db_cur.execute('use %s;' % name)

    def create_table(self, schema):
        for table in schema:
            self._db_cur.execute('create table if not exists %s;' % table)
        self._db_conn.commit()

    def drop_table(self, name):
        self._db_cur.execute('drop table %s;' % name)
        self._db_conn.commit()

    def write_in_table(self, text):
        self._db_cur.execute('insert ignore into %s;' % text)
        self._db_conn.commit()

    def select_all(self, table):
        self._db_cur.execute('select * from %s;' % table)
        return self._db_cur.fetchall()

    def commit(self):
        self._db_conn.commit()