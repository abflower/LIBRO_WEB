"""
This class creates a handler for a mysql database.
"""

from static.db_credentials import credentials
import mysql.connector as connector

class db_handler():

    def __init__(self, name=credentials['user'], passwd=credentials['password']):
        self.user = name
        self.passwd = passwd
        #self.host = host

    def connect(self):

        self._db_conn=connector.connect(user=self.user,passwd=self.passwd)
        self._db_cur = self._db_conn.cursor()

    def close_conn(self):
        self._db_conn.close()

    def commit(self):
        self._db_conn.commit()

    def create_db(self, name):
        self._db_cur.execute('create database if not exists %s;' % name)
        self.commit()

    def use_db(self, name):
        self._db_cur.execute('use %s;' % name)

    def create_table(self, schema):
        for table in schema:
            self._db_cur.execute('create table if not exists %s;' % table)
        self.commit()

    def drop_table(self, name):
        self._db_cur.execute('drop table %s;' % name)
        self._db_conn.commit()

    def write_in_table(self, text):
        self._db_cur.execute('insert ignore into %s;' % text)
        self.commit()

    def select_query(self, col_needed, table, col_search, query):
        self._db_cur.execute("select %s from %s where %s = '%s';" % (col_needed, table, col_search, query))
        return self._db_cur.fetchone()

    def select_all(self, table):
        self._db_cur.execute('select * from %s;' % table)
        return self._db_cur.fetchall()

