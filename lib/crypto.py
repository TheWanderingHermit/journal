__author__     = 'Sidharth Sharma'
__copyright__  = 'Copyright 2019, Sidharth Sharma'
__license__    = 'Beer-Ware License Rev. 42'
__maintainer__ = 'Sidharth Sharma'
__email__      = 'ims.sharma@gmail.com'
__credits__    = ['Sidharth Sharma']
__version__    = '0.1'
__status__     = 'Development'

import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class crypto :
    def __init__( self, password, seed = 16, length = 32, iterations = 1000000 ) :
        """
        Initialize cryptography module

        Parameters : 
        password     ( str ) : password for encryption
        seed         ( int ) : seed for encryption primitive
        length       ( int ) : desired length of the encryption key
        iterations   ( int ) : least number of iterations
        """
        primitive           = PBKDF2HMAC( algorithm=hashes.SHA256(), length=length, salt=os.urandom( seed ), iterations=iterations , backend=default_backend() )
        self.cryptographer  = Fernet( base64.urlsafe_b64encode( primitive.derive( str.encode( password ) ) ) )
    def encrypt( self, string ) :
        """
        Encrypt the supplied string

        Parameters :
        string       ( str ) : unencrypted string
        """
        return self.cryptographer.encrypt( str.encode( string ) )
    def decrypt( self, bytesequence ) :
        """
        Decrypt the supplied string

        Parameters :
        bytesequence ( b )   : encrypted bytesequence
        """
        return ( self.cryptographer.decrypt( bytesequence ) ).decode()
