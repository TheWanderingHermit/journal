import os
import sys

cwd = os.getcwd()
sys.path.append( cwd + "/lib" )

import dbclient
import crypto
import editor


count = 1
def test( test, result ) :
    global count
    print( "Test %d : \t%s\t\t - %s" %( count, test, "passed" if result else "failed" ) )
    count = count + 1

dbc = dbclient.dbclient( os.getcwd() + "/my_test_database.db" )
cryptographer = crypto.crypto( "baby steps" )
text = "Mary had a little lamb"
cyphertext = cryptographer.encrypt( text )
edit = editor.editor()

test( "database connectivity test", dbc != None )
test( "encryption test", text == cryptographer.decrypt( cyphertext ) )
test( "editor test", "abc\ndef\n" == edit.edit( "abc" ) )
