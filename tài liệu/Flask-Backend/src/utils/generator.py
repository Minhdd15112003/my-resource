import random
import string

def String(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def Number(size=6):
    return ''.join(random.choice("0123456789") for _ in range(size))
