# -*- encoding: utf-8 -*-
from app02.threadlocal import thread_local

class MenuMiddlewareItems(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

        try:
            """if 'panecontrol/views/empresa/' in request.path:
                request.session['item'] = 'configuracion'
                request.session['sub_item'] = 'empresa'"""
            pass
        except:
            pass
