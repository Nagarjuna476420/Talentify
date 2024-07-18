import random
import string

def generate_unique_id(prefix):
    unique_id = prefix + ''.join(random.choices(string.ascii_letters + string.digits, k=9))
    return unique_id
