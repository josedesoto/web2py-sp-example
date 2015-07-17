# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    if auth.user:
        message="Welcome: "
        user=auth.user
    else:
        message="Please use login for testing..."
        user=None
    return dict(message=message, user=user)

def metadata():
    import os.path
    if os.path.exists(request.folder + 'private/sp.xml'):
        f = open(request.folder + 'private/sp.xml', 'r')
        response.headers['Content-Type']='application/xml'
        return f.read()
    else:
        import subprocess
        command = 'make_metadata.py ' +  request.folder + 'private/sp_conf.py > ' + request.folder + 'private/sp.xml'
        #In producction should be shell=False
        p=subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
        stdout,stderr = p.communicate()
        status = p.poll()
        if status == 0:
            f = open(request.folder + 'private/sp.xml', 'r')
            response.headers['Content-Type']='application/xml'
            return f.read()
        return str(stderr)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


