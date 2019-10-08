from django.http import HttpResponseRedirect


class MyLoginMiddleware():

    def process_request(self, request):
        if 'user' not in request.session or not request.session['user']:
            return HttpResponseRedirect("http://www.baidu.com")