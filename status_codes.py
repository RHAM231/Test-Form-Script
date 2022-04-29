

from pprint import pprint


class StatusCodes(object):
    def __init__(self):
        # 1xx Informational
        self.informational = {
            # 1xx Informational
            100: 'Continue', 101: 'Switching Protocols', 102: 'Processing',
            102: 'Processing', 103: 'Early Hints'
            }
        # 2xx Successful
        self.successful = {
            200: 'OK', 201: 'Created', 202: 'Accepted',
            203: 'Non-Authoritative Information', 204: 'No Content',
            205: 'Reset Content', 206: 'Partial Content', 207: 'Multi-Status',
            208: 'Already Reported', 226: 'IM Used'
            }
        # 3xx Redirection
        self.redirection = {
            300: 'Multiple Choices', 301: 'Moved Permanently',
            302: 'Found (Previously Moved Temporarily)', 303: 'See Other',
            304: 'Not Modified', 305: 'Use Proxy', 306: 'Switch Proxy',
            307: 'Temporary Redirect', 308: 'Permanent Redirect'
            }
        # 4xx Client Error
        self.client_error = {
            400: 'Bad Request', 401: 'Unauthorized', 402: 'Payment Required',
            403: 'Forbidden', 404: 'Not Found', 405: 'Method Not Allowed',
            406: 'Not Acceptable', 407: 'Proxy Authentication Required',
            408: 'Request Timeout', 409: 'Conflict', 410: 'Gone',
            411: 'Length Required', 412: 'Precondition Failed',
            413: 'Payload Too Large', 414: 'URI Too Long',
            415: 'Unsupported Media Type', 416: 'Range Not Satisfiable',
            417: 'Expectation Failed', 418: 'Im a Teapot',
            421: 'Misdirected Request', 422: 'Unprocessable Entity',
            423: 'Locked', 424: 'Failed Dependency', 425: 'Too Early',
            426: 'Upgrade Required', 428: 'Precondition Required',
            429: 'Too Many Requests', 431: 'Request Header Fields Too Large',
            451: 'Unavailable For Legal Reasons'
            }
        # 5xx Server Error
        self.server_error = {
            500: 'Internal Server Error', 501: 'Not Implemented',
            502: 'Bad Gateway', 503: 'Service Unavailable',
            504: 'Gateway Timeout', 505: 'HTTP Version Not Supported',
            506: 'Variant Also Negotiates', 507: 'Insufficient Storage',
            508: 'Loop Detected', 510: 'Not Extended',
            511: 'Network Authentication Required'
            }

    def get(self, code):
        if 100 <= code <= 199:
            status, name = self.informational, 'Informational'
        elif 200 <= code <= 299:
            status, name = self.successful, 'Successful'
        elif 300 <= code <= 399:
            status, name = self.redirection, 'Redirection'
        elif 400 <= code <= 499:
            status, name = self.client_error, 'Client Error'
        elif 500 <= code <= 599:
            status, name = self.server_error, 'Server Error'
        
        return f'{code} {status[code]} {name}'


SC = StatusCodes()

print(SC.get(200))
