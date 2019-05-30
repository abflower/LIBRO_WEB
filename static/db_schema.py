tables = [
    '''Cities (id int not null auto_increment primary key, city varchar(50), 
    constraint unique_city unique(city))''',

    '''States (id int not null auto_increment primary key, state varchar(50), 
    constraint unique_state unique(state))''',

    '''Languages (id int not null auto_increment primary key, language varchar(20), 
    constraint unique_language unique(language))''',

    '''Publishers (id int not null auto_increment primary key, publisher varchar(20),
    city_id int, constraint unique_pub_city unique(publisher, city_id))''',

    '''LCC (id int not null auto_increment primary key, lcc int, 
    constraint unique_lcc unique(lcc))''',

    '''Dewey (id int not null auto_increment primary key, dewey_class int,
    dewey_subclass int, constraint unique_class_sub unique(dewey_class, dewey_subclass))''',

    '''Authors (id int not null auto_increment primary key, author varchar(65), name varchar(20),
    name_p varchar(5), m_name varchar(20), m_name_p varchar(5), surname varchar (20), trilet varchar(5),
    constraint unique_author unique(author), constraint unique_trilet unique(trilet))'''
]