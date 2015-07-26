# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1437643546.218673
_enable_loop = True
_template_filename = 'htdocs/login.mako'
_template_uri = 'login.mako'
_source_encoding = 'utf-8'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'root.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        redirect_uri = context.get('redirect_uri', UNDEFINED)
        key = context.get('key', UNDEFINED)
        action = context.get('action', UNDEFINED)
        authn_reference = context.get('authn_reference', UNDEFINED)
        login = context.get('login', UNDEFINED)
        password = context.get('password', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n<h1>Please log in</h1>\n<p class="description">\n    To register it\'s quite simple: enter a login and a password\n</p>\n\n<form action="')
        __M_writer(unicode(action))
        __M_writer(u'" method="post">\n    <input type="hidden" name="key" value="')
        __M_writer(unicode(key))
        __M_writer(u'"/>\n    <input type="hidden" name="authn_reference" value="')
        __M_writer(unicode(authn_reference))
        __M_writer(u'"/>\n    <input type="hidden" name="redirect_uri" value="')
        __M_writer(unicode(redirect_uri))
        __M_writer(u'"/>\n\n    <div class="label">\n        <label for="login">Username</label>\n    </div>\n    <div>\n        <input type="text" name="login" value="')
        __M_writer(unicode(login))
        __M_writer(u'" autofocus><br/>\n    </div>\n\n    <div class="label">\n        <label for="password">Password</label>\n    </div>\n    <div>\n        <input type="password" name="password"\n               value="')
        __M_writer(unicode(password))
        __M_writer(u'"/>\n    </div>\n\n    <input class="submit" type="submit" name="form.submitted" value="Log In"/>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"37": 1, "38": 8, "39": 8, "40": 9, "41": 9, "42": 10, "43": 10, "44": 11, "45": 11, "46": 17, "47": 17, "48": 25, "49": 25, "55": 49, "26": 0}, "uri": "login.mako", "filename": "htdocs/login.mako"}
__M_END_METADATA
"""
