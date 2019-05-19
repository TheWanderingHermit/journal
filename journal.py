__author__     = 'Sidharth Sharma'
__copyright__  = 'Copyright 2019, Sidharth Sharma'
__license__    = 'Beer-Ware License Rev. 42'
__maintainer__ = 'Sidharth Sharma'
__email__      = 'ims.sharma@gmail.com'
__credits__    = ['Sidharth Sharma']
__version__    = '0.1'
__status__     = 'Development'

import os
import sys
import tzlocal
import argparse
import datetime

sys.path.append( os.getcwd() + "/lib" )

import dbclient
import crypto
import editor
import queries

class journal :
    def __init__( self, args ) :
        self.getargs( args )
        self.initdb( self.arguments.directory + '/' + self.arguments.repository )
        self.initcrypto()
        self.initeditor()
        self.listlib()
        self.writechapter()

    def getargs( self, args ) : 
        parser = argparse.ArgumentParser( description = "Simply safe journal" )

        parser.add_argument( '-d', '--directory', default = os.getcwd(), help = 'database directory' )
        parser.add_argument( '-r', '--repository', default = 'libraryCentral.db', help = 'database name' )
        parser.add_argument( '-l', '--library', default = 'sid', help = 'library name' )
        parser.add_argument( '-b', '--book', default = str( tzlocal.get_localzone() ), help = 'book to edit' )
        parser.add_argument( '-c', '--chapter', default = datetime.datetime.now().strftime( '%Y%m%d%H%M%S' ), help = 'chapter to edit' )
        parser.add_argument( '-p', '--password', help = 'password to encrypt/decrypt the chapter' )
        parser.add_argument( '-i', '--index', action = 'store_false', help = 'display available libraries ( in the working directory ) and books' )
        self.arguments = parser.parse_args( args )
        print( self.arguments )

    def initdb( self, db ) :
        self.db      = dbclient.dbclient( db )
        self.queries = queries.queries()
        for query in self.queries.createqueries :
            self.db.dbexec( self.queries.queries[ query ] )

    def initcrypto( self ) :
        if self.arguments.password != None :
            self.cryptp = cryptp.crypto( self.arguments.password )
        else :
            self.crypto = None

    def initeditor( self ) :
        self.editor = editor.editor()

    def initlib( self ) :
        self.db.dbexec( self.queries.genquery( 'inlib', self.arguments.library ) )

    def initbook( self ) :
        self.db.dbexec( self.queries.genquery( 'inbook', self.arguments.chapter, self.arguments.book ) )

    def initchapter( self, contents ) :
        self.db.dbexec( self.queries.genquery( 'inchapter', contents, self.arguments.chapter ) )

    def listlib( self ) :
        print( self.db.dbexec( self.queries.genquery( 'lilib', self.arguments.library ) ) )

    def listlib( self ) :
        return self.db.dbexec( self.queries.genquery( 'lilib' ) ) 

    def listbook( self ) :
        return self.db.dbexec( self.queries.genquery( 'libook', self.arguments.book ) ) 

    def listchapter( self, identity ) :
        return self.db.dbexec( self.queries.genquery( 'lichapter', identity ) ) 

    def updatechapter( self, contents, identifier ) :
        self.db.dbexec( self.queries.genquery( 'inchapter', contents, identifier ) )

    def writechapter( self ) :
        self.initlib()
        self.initbook()
        content = self.editor.edit()
        if self.crypto != None :
            content = self.crypto.encrypt( content )
        print( content )
        self.initchapter( content )


if __name__=='__main__' :
    diary = journal( sys.argv[ 1 : ] )
