import random
import string

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_id_generator(instance, new_slug=None):

    unique_id = random_string_generator()
    Klass = instance.__class__
    qs_exist = Klass.objects.filter(instance_unique_id=unique_id).exists()
    if qs_exist:
        return unique_id_generator(instance)
    return unique_id