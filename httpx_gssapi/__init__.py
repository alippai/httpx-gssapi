"""
HTTPX GSSAPI authentication library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

HTTPX is a full featured Python HTTP library with both sync and async APIs
designed to be a next generation HTTP client for Python. This library is a port
of requests_gssapi to HTTPX and adds optional GSSAPI authentication support and
supports mutual authentication. Basic GET usage:

    >>> import httpx
    >>> from httpx_gssapi import HTTPSPNEGOAuth
    >>> r = httpx.get("http://example.org", auth=HTTPSPNEGOAuth())

Both the sync and async HTTPX APIs should be fully supported.
"""
__all__ = (
    'HTTPSPNEGOAuth',
    'HTTPKerberosAuth',
    'MutualAuthenticationError',
    'REQUIRED',
    'OPTIONAL',
    'DISABLED',
)
__version__ = '1.0.0'

import logging

from .gssapi_ import HTTPSPNEGOAuth, REQUIRED, OPTIONAL, DISABLED
from .exceptions import MutualAuthenticationError
from .compat import HTTPKerberosAuth

logging.getLogger(__name__).addHandler(logging.NullHandler())
