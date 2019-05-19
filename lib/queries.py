__author__     = 'Sidharth Sharma'
__copyright__  = 'Copyright 2019, Sidharth Sharma'
__license__    = 'Beer-Ware License Rev. 42'
__maintainer__ = 'Sidharth Sharma'
__email__      = 'ims.sharma@gmail.com'
__credits__    = ['Sidharth Sharma']
__version__    = '0.1'
__status__     = 'Development'

class queries :
    def __init__( self ) :
        self.queries = dict()
        self.queries[ 'a' ] =   """CREATE TABLE IF NOT EXISTS LIBRARY (
                                BOOK TEXT PRIMARY KEY,
                                CREATE_TIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                EDIT_TIME NOT NULL DEFAULT CURRENT_TIMESTAMP
                                ); """
        self.queries[ 'b' ] =   """CREATE TABLE IF NOT EXISTS BOOK (
                                CHAPTER TEXT PRIMARY KEY,
                                BOOK TEXT NOT NULL,
                                CREATE_TIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                EDIT_TIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                FOREIGN KEY( BOOK ) REFERENCES LIBRARY( BOOK )
                                ); """
        self.queries[ 'c' ] =   """CREATE TABLE IF NOT EXISTS CHAPTER (
                                ID INTEGER PRIMARY KEY,
                                CONTENT TEXT NOT NULL,
                                CHAPTER TEXT NOT NULL,
                                CREATE_TIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                EDIT_TIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                FOREIGN KEY( CHAPTER ) REFERENCES BOOK( CHAPTER )
                                ); """
        self.queries[ 'd' ] =   """CREATE TRIGGER IF NOT EXISTS LIBUPDATE AFTER UPDATE ON BOOK
                                BEGIN
                                UPDATE LIBRARY SET EDIT_TIME = CURRENT_TIMESTAMP WHERE BOOK = OLD.BOOK;
                                END; """
        self.queries[ 'e' ] =   """CREATE TRIGGER IF NOT EXISTS BOOKUPDATE AFTER UPDATE ON CHAPTER
                                BEGIN
                                UPDATE BOOK SET EDIT_TIME = CURRENT_TIMESTAMP WHERE CHAPTER = OLD.CHAPTER;
                                END; """
        self.createqueries  = [ 'a', 'b', 'c', 'd', 'e' ]
        self.queries[ 'lilib' ]     =   """SELECT * FROM LIBRARY; """
        self.queries[ 'libook' ]    =   """SELECT * FROM BOOK WHERE CHAPTER LIKE "%s"; """
        self.queries[ 'lichapter' ] =   """SELECT * FROM CHAPTER WHERE ID = %s; """
        self.queries[ 'inlib' ]     =   """INSERT INTO LIBRARY ( BOOK ) VALUES ( '%s' );"""
        self.queries[ 'inbook' ]    =   """INSERT INTO BOOK ( CHAPTER, BOOK ) VALUES ( '%s', '%s' );"""
        self.queries[ 'inchapter' ] =   """INSERT INTO CHAPTER ( CONTENT, CHAPTER ) VALUES ( '%s', '%s' );"""
        self.queries[ 'upchapter' ] =   """UPDATE CHAPTER SET CONTENT = '%s' WHERE ID = %s;"""
    def genquery( self, queryidx, *args ) :
        return self.queries[ queryidx ] % args
