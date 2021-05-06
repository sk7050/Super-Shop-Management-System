from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        path = request.META['PATH_INFO']
        print(path)
        if not request.session.get('user'):
            print ('good')
            return redirect(f'/?return_url={path}')

        response = get_response(request)
        return response
        print('after view')
    return middleware