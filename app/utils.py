from django.conf import settings
from random import choice
from string import ascii_letters, digits

SIZE = getattr(settings, 'MAXIMUM_URL_CHARS', 8)
AVAILABLE_CHARS = ascii_letters + digits

def create_random_code(chars=AVAILABLE_CHARS):
    """
    Creates a random string
    """
    return "".join([choice(chars) for _ in range(SIZE)])


def create_shortened_url(model_instance):
    """
        Create a shortened url for a model instance
    """
    random_code = create_random_code()
    model_class = model_instance.__class__

    if model_class.objects.filter(short_url=random_code).exists():
        return create_shortened_url(model_instance)

    return random_code
