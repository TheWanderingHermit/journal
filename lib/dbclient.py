__author__     = 'Sidharth Sharma'
__copyright__  = 'Copyright 2019, Sidharth Sharma'
__license__    = 'Beer-Ware License Rev. 42'
__maintainer__ = 'Sidharth Sharma'
__email__      = 'ims.sharma@gmail.com'
__credits__    = ['Sidharth Sharma']
__version__    = '0.1'
__status__     = 'Development'

import sqlite3

class dbclient :
    def __init__( self, db ) :
        """
        Initialize database and test connection

        Parameters : 
        db    ( str ) : name
        """
        self.db = db
        try :
            connection = sqlite3.connect( self.db )
        except sqlite3.Error as error :
            raise error
        finally :
            connection.close()
    def dbexec( self, query ) :
        """
        Open a new connection, execute query and close the connection

        Parameter : 
        query ( str ) : query string
        """
        try :
            connection = sqlite3.connect( self.db )
            if connection is not None :
                cursor = connection.cursor()
                cursor.execute( query )
                connection.commit()
                return cursor.fetchall()
        except sqlite3.Error as error :
            raise sqlite3.Error( str( error ) )
        finally :
            connection.close()
