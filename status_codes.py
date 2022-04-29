##############################################################################
# NO IMPORTS, BEGIN CLASSES
##############################################################################


# Set custom colors so we can color code success and fail messages in
# our tabulated results that we print to terminal.
class bcolors(object):
    HEADER = '\033[95m'
    OKBLUE = '\u001b[34m'
    OKCYAN = '\033[96m'
    OKGREEN = '\u001b[32m'
    OKYELLOW = '\u001b[33m'
    WARNING = '\033[93m'
    FAIL = '\u001b[41;1m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Define a class of all possible status codes web requests can return.
# This allows us to print the code and corresponding message to
# terminal.
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

    # Define a get method to color code our messages based on code
    # type.
    def get(self, code):
        # BLue for informational codes.
        if 100 <= code <= 199:
            status, color = self.informational, bcolors.OKBLUE
        # Green for successful codes.
        elif 200 <= code <= 299:
            status, color = self.successful, bcolors.OKGREEN
        # Yellow for redirection codes.
        elif 300 <= code <= 399:
            status, color = self.redirection, bcolors.OKYELLOW
        # And a background of red for client and server error codes.
        elif 400 <= code <= 499:
            status, color = self.client_error, bcolors.FAIL
        elif 500 <= code <= 599:
            status, color = self.server_error, bcolors.FAIL

        return f'{color}{code} {status[code]}{bcolors.ENDC}'


##############################################################################
# END
##############################################################################
