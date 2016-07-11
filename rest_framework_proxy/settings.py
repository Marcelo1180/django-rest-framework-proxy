from django.conf import settings

from rest_framework.settings import APISettings


USER_SETTINGS = getattr(settings, 'REST_PROXY', None)

DEFAULTS = {
    'HOST': None,
    'AUTH': {
        'type': 'Basic',
        'user': None,
        'password': None,
        'token': None,
        # Parametros para tipo JWT
        'num_attemps': 1,
        'auth_url': None,
        'auth_credentials': None,
        'jwt_auth_header_prefix': 'Bearer'
    },
    'TIMEOUT': None,
    'DEFAULT_HTTP_ACCEPT': 'application/json',
    'DEFAULT_HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.8',
    'DEFAULT_CONTENT_TYPE': 'text/plain',

    # Return response as-is if enabled
    'RETURN_RAW': False,

    # Used to translate Accept HTTP field
    'ACCEPT_MAPS': {
        'text/html': 'application/json',
    },

    # Do not pass following parameters
    'DISALLOWED_PARAMS': ('format',),

    # Perform a SSL Cert Verification on URI requests are being proxied to
    'VERIFY_SSL': True,
}

api_proxy_settings = APISettings(USER_SETTINGS, DEFAULTS)
