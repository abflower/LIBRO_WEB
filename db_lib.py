import MySQLdb
conn=MySQLdb.connect(host='localhost',user='dbadmin',passwd='password')
cursor = conn.cursor()


def create_db(name):
    cursor.execute('Create database %s' % name)


def use_db(name):
    cursor.execute('use %s' % name)


def drop_tables():
    cursor.executescript('''
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
    conn.commit()


def create_tables():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Author
    (id int PRIMARY KEY, author varchar(50), name varchar(20),
    mid_name varchar(20), surname varchar(20), trilet varchar(5), UNIQUE(author, trilet))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS City
    (id int PRIMARY KEY, city varchar(50), UNIQUE(city))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS State
    (id int PRIMARY KEY, state varchar(50), UNIQUE(state))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Publisher
    (id int PRIMARY KEY, publisher varchar(50), city_id int, state_id int, CONSTRAINT Pub_city UNIQUE(publisher, city_id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Language
    (id int PRIMARY KEY, language varchar(20) UNIQUE)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Dewey
    (id int PRIMARY KEY, dewey_unique varchar(20) UNIQUE, class_ varchar(5), subclass varchar(15), CONSTRAINT Class_sub UNIQUE(class_, subclass))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS LCC
    (id int PRIMARY KEY, lcc varchar(10) UNIQUE)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Book
    (id int PRIMARY KEY, library_code varchar(10), title varchar(100), title_long varchar(200),
    volume int, year int, publisher_id int, pages int, language_id int,
    dewey_id int, lcc_id int, isbn_10 int, isbn_13 int)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Author_book
    (id int PRIMARY KEY, author_id int, book_id int, CONSTRAINT Authorship UNIQUE(author_id, book_id))''')

    conn.commit()


def close_connection():
    conn.close()


