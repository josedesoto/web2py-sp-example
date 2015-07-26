#!/usr/bin/env python
# -*- coding: utf-8 -*-

## SP CONFIGURATION ##
from saml2 import BINDING_HTTP_POST, BINDING_HTTP_REDIRECT
import os.path
import requests
import tempfile

# To load the IDP metadata in case Okta: http://idp.oktadev.com/metadata
idp = 'http://localhost:8088/metadata'
try:
    rv = requests.get(idp)
except:
    #In case the local IDP is not running yet we take the local file
    import argparse as ap
    aux = {'name': 'IDP/idp.xml'}
    tmp = ap.Namespace(**aux)
else:
    tmp = tempfile.NamedTemporaryFile()
    f = open(tmp.name, 'w')
    f.write(rv.text)
    f.close()

BASEDIR = os.path.abspath(os.path.dirname(__file__))

def full_path(local_file):
    return os.path.join(BASEDIR, local_file)


CONFIG = {                
    # your entity id, usually your subdomain plus the url to the metadata view, change Change your ngrok subdomain in case you test with Okta
    'entityid': 'http://localhost:8088/sp/default/metadata',
    'service': {
        'sp' : {
            'name': 'MYSP',  
            'endpoints': {     
                'assertion_consumer_service': [
                    #Change your ngrok subdomain o localhost in case you test with LOCAL IDP
                    ('http://localhost:8000/sp/default/user/login', BINDING_HTTP_REDIRECT),
                    ('http://localhost:8000/sp/default/user/login', BINDING_HTTP_POST),       
                    ],
                },
            # Don't verify that the incoming requests originate from us via the built-in cache for authn request ids in pysaml2. Be carefull in producction!!!
            'allow_unsolicited': True,
            },
        },
    'key_file': full_path('pki/mykey.pem'),
    'cert_file': full_path('pki/mycert.pem'),
    # where the remote metadata is stored
    'metadata': {
         'local': [tmp.name],
        },
}


