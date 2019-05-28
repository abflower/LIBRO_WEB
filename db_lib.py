import MySQLdb

class db_handler:

    def __init__(self):
        self.host = 'localhost'
        self.user = 'dbadmin'
        self.passwd = 'password'
        self._db_conn=MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd)
        self._db_cur = self._db_conn.self._db_cur()

    def create_db(self, name):
        self._db_cur.execute('Create database %s' % name)

    def use_db(self, name):
        self._db_cur.execute('use %s' % name)


    def drop_tables(self):
        self._db_cur.executescript('''
        DROP TABLE IF EXISTS Author;
        DROP TABLE IF EXISTS Book;
        DROP TABLE IF EXISTS Author_book;
        DROP TABLE IF EXISTS City;
        DROP TABLE IF EXISTS Dewey;
        DROP TABLE IF EXISTS LCC;
        DROP TABLE IF EXISTS Language;
        DROP TABLE IF EXISTS Publisher;
        DROP TABLE IF EXISTS State;
        ''')
        self._db_conn.commit()
    
    
    def create_tables(self):
        self._db_cur.execute('''CREATE TABLE IF NOT EXISTS Author
        (id int PRIMARY KEY, author varchar(50), name varchar(20),
        mid_name varchar(20), surname varchar(20), trilet varchar(5), UNIQUE(author, trilet))''')
    
        self._db_cur.execute('''CREATE TABLE IF NOT EXISTS City
        (id int PRIMARY KEY, city varchar(50), UNIQUE(city))''')
    
        self._db_cur.execute('''CREATE TABLE IF NOT EXISTS State
        (id int PRIMARY KEY, state varchar(50), UNIQUE(state))''')
    
        self._db_cur.execute('''CREATE TABLE IF NOT EXISTS Publisher
        (id int PRIMARY KEY, publisher varchar(50), city_id int, state_id int, CONSTRAINT Pub_city UNIQUE(publisher, city_id))''')
    
        self._db_cur.execute('''CREATE TABLE IF NOT EXISTS Language
        (id int PRIMARY KEY, language varchar(20) UNIQUE)''')
    
        self._db_cur.execute('''CREATE TABLE IF NOT EXISTS Dewey
        (id int PRIMARY KEY, dewey_unique varchar(20) UNIQUE, class_ varchar(5), subclass varchar(15), CONSTRAINT Class_sub UNIQUE(class_, subclass))''')
    
        self._db_cur.execute('''CREATE TABLE IF NOT EXISTS LCC
        (id int PRIMARY KEY, lcc varchar(10) UNIQUE)''')
    
        self._db_cur.execute('''CREATE TABLE IF NOT EXISTS Book
        (id int PRIMARY KEY, library_code varchar(10), title varchar(100), title_long varchar(200),
        volume int, year int, publisher_id int, pages int, language_id int,
        dewey_id int, lcc_id int, isbn_10 int, isbn_13 int)''')
    
        self._db_cur.execute('''CREATE TABLE IF NOT EXISTS Author_book
        (id int PRIMARY KEY, author_id int, book_id int, CONSTRAINT Authorship UNIQUE(author_id, book_id))''')
    
        self._db_conn.commit()
    
    
    def write_in_table(self, table, value1):
        self._db_cur.execute('''INSERT INTO %s VALUES %s
        ''' % (table, value1))
    
    def close_connection(self):
        self._db_conn.close()
    
    
