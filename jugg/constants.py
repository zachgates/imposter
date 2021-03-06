# System
NAME_REGEX = r'\w{1,32}'

# Commands
CMD_SHAKE = -1
CMD_ERR = 0
CMD_RESP = 1
CMD_AUTH = 2

CMD_2_NAME = {
    CMD_SHAKE: 'handshake',
    CMD_ERR: 'error',
    CMD_RESP: 'response',
    CMD_AUTH: 'authenticate',
}

# Error codes
ERR_NO_CONNECTION = -1
ERR_DISCONNECT = 0
ERR_CREDENTIALS = 1
ERR_HMAC = 2
ERR_CHALLENGE = 3
ERR_VERIFICATION = 4

ERROR_INFO_MAP = {
    ERR_NO_CONNECTION: 'could not connect',
    ERR_DISCONNECT: 'disconnected by server',
    ERR_CREDENTIALS: 'invalid credentials',
    ERR_HMAC: 'invalid hmac',
    ERR_CHALLENGE: 'failed challenge',
    ERR_VERIFICATION: 'failed verification',
}


__all__ = [
    # System
    'NAME_REGEX',
    # Commands
    'CMD_SHAKE', 'CMD_ERR', 'CMD_RESP', 'CMD_AUTH',
    'CMD_2_NAME',
    # Error codes
    'ERR_NO_CONNECTION', 'ERR_DISCONNECT', 'ERR_CREDENTIALS', 'ERR_HMAC',
    'ERR_CHALLENGE', 'ERR_VERIFICATION', 'ERROR_INFO_MAP',
]
