from django.core.exceptions import VallidationError
def min_length_validator(value):
    if len(value) != 16:
        raise VallidationError("length is not 16")