"""
Genertate a hash based on sha1
"""

import hashlib
import time

filename = 'hello.png'

now = str(time.time())

m = hashlib.sha1()
m.update((now + filename).encode('utf-8'))
m.hexdigest()
