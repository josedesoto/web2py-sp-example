#!/usr/bin/env python
# -*- coding: utf-8 -*-

## SP CONFIGURATION ##
from saml2 import BINDING_HTTP_POST, BINDING_HTTP_REDIRECT
import os.path
import requests
import tempfile

# To load the IDP metadata
idp = 'http://idp.oktadev.com/metadata'
rv = requests.get(idp)
tmp = tempfile.NamedTemporaryFile()
f = open(tmp.name, 'w')
f.write(rv.text)
f.close()

BASEDIR = os.path.abspath(os.path.dirname(__file__))

def full_path(local_file):
    return os.path.join(BASEDIR, local_file)


CONFIG = {                
    # your entity id, usually your subdomain plus the url to the metadata view
    'entityid': 'http://2cf3577a.ngrok.com/sp/default/metadata',
    'service': {
        'sp' : {
            'name': 'MYSP',  
            'endpoints': {     
                'assertion_consumer_service': [
                    #Change your ngrok subdomain
                    ('http://2cf3577a.ngrok.com/sp/default/user/login', BINDING_HTTP_REDIRECT),
                    ('http://2cf3577a.ngrok.com/sp/default/user/login', BINDING_HTTP_POST),       
                    ],
                },
            # Don't verify that the incoming requests originate from us via the built-in cache for authn request ids in pysaml2. Be carefull in producction!!!
            'allow_unsolicited': True,

            # in this section the list of IdPs we talk to are defined
            'idpsso': {
                # the keys of this dictionary are entity ids
                'urn:example:idp': {
                    'single_sign_on_service': {
                        BINDING_HTTP_REDIRECT: 'http://idp.oktadev.com',
                        },
                    },
                },
            },
        },
    'key_file': full_path('pki/mykey.pem'),
    'cert_file': full_path('pki/mycert.pem'),
    # where the remote metadata is stored
    'metadata': {
         'local': [tmp.name],
        },
}


