def validate_age(age):
    if age > 0:
        return age
    if age < 0:
        raise ValueError('Age can not be less than 0')


def validate_phone(phonenumber):
    if phonenumber < 0:
        raise ValueError('Age can not be less than 0')


def tesint_raise():
    try:
        validate_age(-1)
        validate_phone(-1)
    except ValueError:
        print('Error')
