# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1437643546.237452
_enable_loop = True
_template_filename = u'templates/root.mako'
_template_uri = u'root.mako'
_source_encoding = 'utf-8'
_exports = ['css_link', 'pre', 'post', 'css']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def pre():
            return render_pre(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        set = context.get('set', UNDEFINED)
        def post():
            return render_post(context._locals(__M_locals))
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        self.seen_css = set() 
        
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'<html>\n<head><title>IDP test login</title>\n    ')
        __M_writer(unicode(self.css()))
        __M_writer(u'\n    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n</head>\n<body>\n    ')
        __M_writer(unicode(pre()))
        __M_writer(u'\n')
        __M_writer(unicode(next.body()))
        __M_writer(u'\n')
        __M_writer(unicode(post()))
        __M_writer(u'\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css_link(context,path,media=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        context._push_buffer()
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if path not in self.seen_css:
            __M_writer(u'        <link rel="stylesheet" type="text/css" href="')
            __M_writer(filters.html_escape(unicode(path)))
            __M_writer(u'" media="')
            __M_writer(unicode(media))
            __M_writer(u'">\n')
        __M_writer(u'    ')
        self.seen_css.add(path) 
        
        __M_writer(u'\n')
    finally:
        __M_buf, __M_writer = context._pop_buffer_and_writer()
        context.caller_stack._pop_frame()
    __M_writer(filters.trim(__M_buf.getvalue()))
    return ''


def render_pre(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        context._push_buffer()
        __M_writer = context.writer()
        __M_writer(u'\n    <div class="header">\n        <h1><a href="/">Login</a></h1>\n    </div>\n')
    finally:
        __M_buf, __M_writer = context._pop_buffer_and_writer()
        context.caller_stack._pop_frame()
    __M_writer(filters.trim(__M_buf.getvalue()))
    return ''


def render_post(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        context._push_buffer()
        __M_writer = context.writer()
        __M_writer(u'\n    <div>\n        <div class="footer">\n            <p>&#169; Copyright 2014 Ume&#229; Universitet &nbsp;</p>\n        </div>\n    </div>\n')
    finally:
        __M_buf, __M_writer = context._pop_buffer_and_writer()
        context.caller_stack._pop_frame()
    __M_writer(filters.trim(__M_buf.getvalue()))
    return ''


def render_css(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        context._push_buffer()
        def css_link(path,media=''):
            return render_css_link(context,path,media)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(css_link('/static/css/main.css', 'screen')))
        __M_writer(u'\n')
    finally:
        __M_buf, __M_writer = context._pop_buffer_and_writer()
        context.caller_stack._pop_frame()
    __M_writer(filters.trim(__M_buf.getvalue()))
    return ''


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"15": 0, "27": 1, "29": 1, "30": 7, "31": 10, "32": 15, "33": 22, "34": 25, "35": 27, "36": 27, "37": 31, "38": 31, "39": 34, "40": 34, "41": 35, "42": 35, "48": 2, "54": 2, "55": 3, "56": 4, "57": 4, "58": 4, "59": 4, "60": 4, "61": 6, "62": 6, "64": 6, "72": 11, "77": 11, "85": 16, "90": 16, "98": 8, "105": 8, "106": 9, "107": 9, "115": 107}, "uri": "root.mako", "filename": "templates/root.mako"}
__M_END_METADATA
"""
