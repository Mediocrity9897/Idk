from django.http import HttpRequest


def set_useragent_on_request_middleware(get_response):
    print("initial call")

    def middleware(request: HttpRequest):
        print("before get response")
        request.user_agent = request.META["HTTP_USER_AGENT"]
        response = get_response(request)
        print("after get response")
        return response
    
    return middleware

class CountRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.responses_cont = 0
        self.exeptions_count = 0
    
    def __call__(self, request: HttpRequest ):
        self.requests_count += 1
        print("requests count: ", self.requests_count)
        response = self.get_response(request)
        self.responses_cont += 1
        print("response count: ", self.responses_cont)
        return response
    
    def poccess_exception(self, request: HttpRequest, exception: Exception):
        self.exeptions_count += 1
        print('Got ', self.exeptions_count, 'exceptions so far')