from django.core.exceptions import ValidationError


def check_phone_number(value):
    if not isinstance(value, str):
        raise ValidationError(f'{value} must be string.')
    if not value.isdigit():
        raise ValidationError(f'{value} must be number.')
    if not value.startswith('09'):
        raise ValidationError(f'{value} must started with "09".')
    