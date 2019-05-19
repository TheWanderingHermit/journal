__author__     = 'Sidharth Sharma'
__copyright__  = 'Copyright 2019, Sidharth Sharma'
__license__    = 'Beer-Ware License Rev. 42'
__maintainer__ = 'Sidharth Sharma'
__email__      = 'ims.sharma@gmail.com'
__credits__    = ['Sidharth Sharma']
__version__    = '0.1'
__status__     = 'Development'

import sys, tempfile, os
import subprocess

class editor :
    def __init__( self, default_editor = 'vim' ) :
        """
        Set the default editor of choice

        Parameters :
        default_editor ( str ) : editor
        """
        self.editor = os.environ.get( 'EDITOR', default_editor )
    def edit( self, initial_message = "" ) :
        """
        Use the editor to input the string

        Parameters :
        initial_message ( str ) : initial message for the ditor

        Return :
        string          ( str ) : edit string
        """
        initial_message = str.encode( initial_message )
        with tempfile.NamedTemporaryFile( suffix = ".tmp" ) as temp_fh :
            temp_fh.write( initial_message )
            temp_fh.flush()
            out, err = subprocess.Popen( [ self.editor, '+set backupcopy=yes', temp_fh.name ] ).communicate()
            if err != None :
                raise IOError( "failed IO\n" + err );
            temp_fh.seek( 0 )
            string = temp_fh.read().decode()
        temp_fh.close()
        return string
