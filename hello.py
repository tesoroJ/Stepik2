def app(environ, start_response):
    start_response("200 OK", [
        ("Content-Type", "text/plain")
    ])
    resp = environ['QUERY_STRING'].split("&")
    resp = [item + '\r\n' for item in resp]
    return resp


# def app(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')),
#                   encoding="utf8")]