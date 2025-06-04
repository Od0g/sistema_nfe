#para gerar uma SECRET_KEY forte no Python, você pode usar:

#Python

import os
print(os.urandom(24).hex())